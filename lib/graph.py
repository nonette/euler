from collections import defaultdict
import heapq


class Graph:
    """A graph, with optionally weighted nodes and edges.
    Nodes are by default weight 0.
    Edges are by default weight 1."""

    def __init__(self, nodes=None, edges=None, node_values=None,
            edge_values=None):
        """Initialize graph.
        Optionally, takes an iterator of nodes, an iterator of edges (pairs of nodes), and
        dictionaries of node_values and edge_values"""
        if nodes is None:
            nodes = []
        self.nodes = set(nodes)
        self.edges = defaultdict(set)
        if edges:
                self.add_edges(edges)
        if node_values is None:
            node_values = defaultdict(int)
        self.node_values = node_values
        
        if edge_values is None:
            edge_values = defaultdict(lambda: 1)
        self.edge_values = edge_values

    def __repr__(self):
        return ('Nodes: %s\nEdges: %s\nNode values %s\nEdge values %s' %
            (str(self.nodes), str(self.edges), str(self.node_values), 
                str(self.edge_values)))

    def add_node(self, node, node_value=None):
        self.nodes.add(node)
        if node_value:
            self.node_values[node] = node_value

    def add_edge(self, a, b, edge_value=None):
        if a not in self.nodes:
            self.nodes.add(a)
        if b not in self.nodes:
            self.nodes.add(b)
        self.edges[a].add(b)
        if edge_value:
            self.edge_values[(a,b)] = edge_value

    def add_edges(self, edges, edge_values=None):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def shortestpath(self, a, b):
        """Dijkstra's.
        Returns sum of edge weights and node weights from a to b, inclusive.
        Return -1 if there is no path from a to b."""
        # implemented with a simple heap (no decrease-key)
        # so there can be stale entries
        # need to check if node already visited
        distances = {a:self.node_values[a]}
        to_visit = [(self.node_values[a],a)]
        visited = set([])
        while len(to_visit) > 0:
            cur_d, cur_node = heapq.heappop(to_visit)
            if cur_node in visited:
                continue
            if cur_node == b:
                return cur_d
            for nbr in self.edges[cur_node]:
                distance = (cur_d + 
                        self.edge_values[(cur_node, nbr)] +
                        self.node_values[nbr])
                if nbr not in distances or distances[nbr] > distance:
                    distances[nbr] = distance
                    heapq.heappush(to_visit, (distance, nbr))
            visited.add(cur_node)
        return -1                    

    def top_sort(self):
        """Return a good top sort, or None if graph is not a dag"""
        unvisited = set(self.nodes)
        marked = set([])
        ret_val = []

        def visit(node):
            """Visit a node; return True if all is well, False if a cycle is
            detected"""
            if node in marked:
                return False
            if node not in unvisited:
                return True
            marked.add(node)
            for nbr in self.edges[node]:
                if not visit(nbr):
                    return False
            ret_val.append(node)
            marked.remove(node)
            unvisited.remove(node)
            return True

        while len(unvisited) != 0:
            node = unvisited.pop()
            unvisited.add(node)
            if not visit(node):
                return None
        return ret_val[::-1]



# Find the shortest passcode that contains the given keylogs as substrings
# (nonconsecutive but inorder)
#
# Let's assume that the passcode has no repeating digits. If it did...

from collections import defaultdict

filename = 'p079keylog.txt'

class Graph:
    def __init__(self, nodes=None, edges=None):
        if not nodes:
            nodes = []
        self.nodes = set(nodes)
        self.edges = defaultdict(set)
        if edges:
                self.add_edges(edges)

    def add_edge(self, edge):
        a,b = edge
        if a not in self.nodes:
            self.nodes.add(a)
        if b not in self.nodes:
            self.nodes.add(b)
        self.edges[a].add(b)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

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


def p079():
    with open(filename) as f:
        raw = f.read().splitlines()
    digits = set(''.join(raw))
   
    graph = Graph(digits)
    for a,b,c in raw:
        graph.add_edges([(a,b),(b,c),(a,c)])
    return ''.join(graph.top_sort())


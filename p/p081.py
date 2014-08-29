# Find the minimum path sum from the top left to the bottom right corner in the
# matrix in the included file.

from collections import defaultdict

import lib.graph as graph

test="""131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331"""
test = [[int(d) for d in line.split()] for line in test.splitlines()]

filename = "resources/matrix.txt"

def readmatrix(filename):
    with open(filename) as f:
        raw = f.read()
        matrix = [[int(d) for d in line.split(',')] for line in raw.splitlines()]
    return matrix

def buildgraph(matrix):
    g = graph.Graph(edge_values=defaultdict(int))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            g.add_node((i,j), matrix[i][j])
            if i+1 < len(matrix):
                g.add_edge((i,j), (i+1,j))
            if j+1 < len(matrix[0]):
                g.add_edge((i,j), (i,j+1))
    return g

def p081(matrix=None):
    if not matrix:
        matrix = readmatrix(filename)
    g = buildgraph(matrix)
    return g.shortestpath((0,0), (len(matrix)-1, len(matrix[0])-1))

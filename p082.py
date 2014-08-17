# Find the minimum path sum from the left to the right in the
# matrix in the included file.

import graph
import p081

filename = 'matrix.txt'

def buildgraph(matrix):
    g = p081.buildgraph(matrix)
    for i in range(1,len(matrix)):
        for j in range(len(matrix[0])):
            g.add_edge((i,j),(i-1,j))
    g.add_node('source', 0)
    for i in range(len(matrix)):
        g.add_edge('source',(i,0))
    g.add_node('sink',0)
    for i in range(len(matrix)):
        g.add_edge((i,len(matrix[0])-1),'sink')
    return g

def p082(matrix=None):
    if not matrix:
        matrix = p081.readmatrix(filename)
    g = buildgraph(matrix)
    return g.shortestpath('source', 'sink')

# Find the minimum path sum from the top left to the bottom right in the
# matrix in the included file.

import graph
import p081

filename='matrix.txt'

def buildgraph(matrix):
    g = p081.buildgraph(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i-1 >= 0:
                g.add_edge((i,j),(i-1,j))
            if j-1 >= 0:
                g.add_edge((i,j),(i,j-1))
    return g

def p083(matrix=None):
    if not matrix:
        matrix = p081.readmatrix(filename)
    g = buildgraph(matrix)
    return g.shortestpath((0,0), (len(matrix)-1,len(matrix[0])-1))

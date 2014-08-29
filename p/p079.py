# Find the shortest passcode that contains the given keylogs as substrings
# (nonconsecutive but inorder)
#
# Let's assume that the passcode has no repeating digits. If it did...

import lib.graph as graph

filename = 'resources/p079keylog.txt'

def p079():
    with open(filename) as f:
        raw = f.read().splitlines()
    digits = set(''.join(raw))
   
    g = graph.Graph(digits)
    for a,b,c in raw:
        g.add_edges([(a,b),(b,c),(a,c)])
    return ''.join(g.top_sort())


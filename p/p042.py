## Count the triangle words in the included file
#
# Solution: 162

import logging

import p022

logger = logging.getLogger(__name__)

def p042(filename='resources/p042words.txt'):
    words = p022.readnames(filename)

    longestword = max(len(word) for word in words)
    upper = 26*longestword
    triangles = [1]
    while triangles[-1] < upper:
        triangles.append(triangles[-1]+len(triangles)+1)
    
    count = 0
    for word in words:
        if p022.namescore(word) in triangles:
            logger.debug(word) 
            count += 1
    return count
        


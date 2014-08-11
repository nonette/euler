## Solve the given sudoku puzzles.

import copy
import sys

## precalculate neighbors
neighbors = {}
for a in range(9):
    for b in range(9):
        square = (a,b)
        neighbors[square] = []
        for i in range(9):
            col_neighbor = (i,square[1])
            if col_neighbor != square:
                neighbors[square].append(col_neighbor)
            row_neighbor = (square[0],i)
            if row_neighbor != square:
                neighbors[square].append(row_neighbor)
        subsquare = (square[0]/3, square[1]/3)
        for i in range(3):
            for j in range(3):
                subsquare_neighbor = (3*subsquare[0]+i,
                        3*subsquare[1]+j)
                if subsquare_neighbor != square:
                    neighbors[square].append(subsquare_neighbor)
for k in neighbors:
    neighbors[k] = list(set(neighbors[k]))

def prettyprint(solution):
    for i in range(9):
        print ' '.join(str(solution[(i,j)]) for j in range(9))

## initialize squares with all possibilities available at every square
#  go through and assign the given values
def solve(board):
    squares = dict(((i,j), range(1,10)) for i in range(9) for j in range(9))
    for row in range(len(board)):
        for col in range(len(board)):           
            if board[row][col] != 0:      
                if not assign(squares, (row,col), board[row][col]):
                    return False
    return solvehelper(squares)
    
def solvehelper(squares):
    if not squares:
        return None
    if all(len(squares[s]) == 1 for s in squares):
        return squares
    square = min(s for s in squares if len(squares[s]) > 1)
    for possibility in squares[square]:
        solution = solvehelper(assign(copy.deepcopy(squares), square, possibility))
        if solution:
            return solution
    return None

def assign(squares, square, possibility):
    squares[square] = [possibility]
    for neighbor in neighbors[square]:
        if not eliminate(squares, neighbor, possibility):
            return None
    return squares

def eliminate(squares, square, possibility):
    if possibility not in squares[square]:
        return squares
    squares[square].remove(possibility)
    if len(squares[square]) == 0:
        return None
    if len(squares[square]) == 1:
        if not assign(squares, square, squares[square][0]):
            return None
    return squares

def p096(filename = 'p096sudoku.txt'):
    with open(filename) as f:
        raw = f.read()
    raw = raw.splitlines()
    sudokus = []
    i = 1
    while i < len(raw):
        sudokus.append([[int(d) for d in raw[i+j]] for j in range(9)])
        i += 10

    count = 0
    for sudoku in sudokus:
        solution = solve(sudoku)
        val = 100*solution[(0,0)][0]+10*solution[(0,1)][0]+solution[(0,2)][0]
        count += val
    return count

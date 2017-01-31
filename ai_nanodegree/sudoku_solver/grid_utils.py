#!/usr/bin/env python

'''
Camilo F. Buscaron
1/17/2017
Sodoku Solver
'''

from __future__ import print_function

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)
print('boxes:')
print(boxes)

row_units = [cross(r, cols) for r in rows]
print('row_units:')
#print(row_units)

column_units = [cross(rows, c) for c in cols]
print('column_units:')
#print(column_units)

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
print('square_units:')
#print(square_units)

unitlist = row_units + column_units + square_units
print('unitlist:')
#print(unitlist)

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
print('units:')
#print(units)

peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
print('peers:')
#print(peers)

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
        ex: '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"

    zip_them = zip(boxes, grid)
    print(zip_them)
    arranged_dict = dict(zip_them)
    print(arranged_dict)
    return arranged_dict

display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

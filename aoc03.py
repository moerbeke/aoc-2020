#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 3

########################################################################
# Algorithms
########################################################################

from collections import namedtuple
P = namedtuple('P', ['x', 'y'])

TREE = '#'
OPEN = '.'

def parse_input(input_str):
    global _tmap
    global _end_x
    global _end_y
    _tmap = dict()
    y = 0
    for line in input_str.strip().split('\n'):
        x = 0
        for c in line:
            _tmap[P(x,y)] = c
            x += 1
        _end_x = x
        y += 1
    _end_y = y

def reset():
    return

def solve_1():
    n_trees = 0
    x = 0
    y = 0
    inc_x = 3
    inc_y = 1
    while y < _end_y:
        p = P(x % _end_x, y)
        n_trees += (_tmap[p] == TREE)
        x += inc_x
        y += inc_y
    return n_trees

def solve_2():
    '''
    Right 1, down 1.
    Right 3, down 1.
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    '''
    slopes = [
            P(1,1),
            P(3,1),
            P(5,1),
            P(7,1),
            P(1,2)]
    prod = 1
    for s in slopes:
        n_trees = 0
        x = 0
        y = 0
        inc_x = s.x
        inc_y = s.y
        while y < _end_y:
            p = P(x % _end_x, y)
            n_trees += (_tmap[p] == TREE)
            x += inc_x
            y += inc_y
        prod *= n_trees
    return prod

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

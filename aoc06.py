#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 6

########################################################################
# Algorithms
########################################################################

_questions = 'abcdefghijklmnopqrstuvwxyz'

def parse_input(input_str):
    global _groups
    _groups = list()
    group = list()
    input_str = input_str.strip() + '\n'
    for line in input_str.split('\n'):
        if len(line) > 0:
            group.append(set(line))
        else:
            _groups.append(group)
            group = list()

def reset():
    return

def count_yes_any(group):
    n = 0
    answers = set.union(*group)
    for q in _questions:
        if q in answers:
            n += 1
    return n

def count_yes_all(group):
    n = 0
    answers = set.intersection(*group)
    for q in _questions:
        if q in answers:
            n += 1
    return n

def solve_1():
    n = 0
    for g in _groups:
        n += count_yes_any(g)
    return n

def solve_2():
    n = 0
    for g in _groups:
        n += count_yes_all(g)
    return n

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

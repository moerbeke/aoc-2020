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

def parse_input(input_str):
    global _groups
    global _people
    _groups = list()
    _people = list()
    i = 0
    new_group = True
    _groups.append('')
    _people.append(list())
    input_str = input_str.strip() + '\n'
    for line in input_str.split('\n'):
        if len(line) > 0:
            if new_group:
                _groups.append('')
                _people.append(list())
                new_group = False
            _groups[i] += line
            _people[i].append(set(line))
        else:
            new_group = True
            i += 1

def reset():
    return

def count_yes_any(group):
    n = 0
    questions = 'abcdefghijklmnopqrstuvwxyz'
    for q in questions:
        if q in group:
            n += 1
    return n

def count_yes_all(group):
    n = 0
    questions = 'abcdefghijklmnopqrstuvwxyz'
    if len(group) > 0:
        people = set.intersection(*group)
        for q in questions:
            if q in people:
                n += 1
    return n

def solve_1():
    n = 0
    for g in _groups:
        n += count_yes_any(g)
    return n

def solve_2():
    n = 0
    for g in _people:
        n += count_yes_all(g)
    return n

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

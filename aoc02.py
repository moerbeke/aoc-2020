#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 2

########################################################################
# Algorithms
########################################################################

def parse_input(input_str):
    '''
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    '''
    global _lines
    _lines = input_str.strip().split('\n')

def reset():
    return

def solve_1():
    n = 0
    for line in _lines:
        times, letter, password = line.split(' ')
        min_times, max_times = [int(t) for t in times.split('-')]
        letter = letter[0]
        n_times = password.count(letter)
        if n_times >= min_times and n_times <= max_times:
            n += 1
    return n

def solve_2():
    n = 0
    for line in _lines:
        pos, letter, password = line.split(' ')
        i, j = [int(p) for p in pos.split('-')]
        letter = letter[0]
        if (letter == password[i-1] or letter == password[j-1]) and not (letter == password[i-1] and letter == password[j-1]):
            n += 1
    return n

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

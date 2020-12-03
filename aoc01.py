#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 1

########################################################################
# Algorithms
########################################################################

_N = 2020

def parse_input(input_str):
    global _numbers
    _numbers = [int(n) for n in input_str.strip().split('\n')]

def reset():
    return

def solve_1():
    n = len(_numbers)
    for i in range(0, n):
        for j in range(1, n):
            if i != j and _numbers[i] + _numbers[j] == _N:
                return _numbers[i] * _numbers[j]

def solve_2():
    n = len(_numbers)
    for i in range(0, n):
        for j in range(1, n):
            for k in range(2, n):
                if i != j and i != k and j != k and _numbers[i] + _numbers[j] + _numbers[k] == _N:
                    return _numbers[i] * _numbers[j] * _numbers[k]


########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

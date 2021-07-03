#!/usr/bin/env python3

########################################################################
# Advent of Code 2021 - solver
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

day = 9

########################################################################
# Algorithms
########################################################################

_preamble_len = 25

def set_preamble(n):
    global _preamble_len
    _preamble_len = n

def parse_input(input_str):
    global _numbers
    _numbers = [int(line) for line in input_str.strip().split('\n')]

def is_valid(pos):
    code = _numbers[pos-_preamble_len:pos]
    n = _numbers[pos]
    valid = False
    for i in range(0, len(code)-1):
        for j in range(i+1, len(code)):
            if code[i] != code[j] and code[i] + code[j] == n:
                valid = True
                break
        if valid:
            break
    return valid

def find_bad_pos():
    assert(len(_numbers) > _preamble_len)
    for pos in range(_preamble_len, len(_numbers)):
        if not is_valid(pos):
            return pos
    return None

def solve_1():
    return _numbers[find_bad_pos()]

def solve_2():
    bad_pos = find_bad_pos()
    bad_number = _numbers[bad_pos]
    weakness = 0
    for i in range(0, bad_pos-1):
        for j in range(i+1, bad_pos):
            first_numbers = _numbers[i:j+1]
            sum_fn = sum(first_numbers)
            if sum_fn >= bad_number:
                if sum_fn == bad_number:
                    weakness = min(first_numbers) + max(first_numbers)
                break
        if weakness > 0:
            break
    return weakness

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

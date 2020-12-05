#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 5

########################################################################
# Algorithms
########################################################################

def parse_input(input_str):
    global _seats
    _seats = [s for s in input_str.strip().split('\n')]

def reset():
    return

def solve_1():
    max_sid = 0
    for s in _seats:
        s = s.replace('F', '0')
        s = s.replace('B', '1')
        s = s.replace('L', '0')
        s = s.replace('R', '1')
        row = int(s[0:7], 2)
        c = int(s[7:], 2)
        sid = row * 8 + c
        if sid > max_sid:
            max_sid = sid
    return max_sid

def solve_2():
    min_sid = 128*8
    max_sid = 0
    existing_sids = []
    for s in _seats:
        s = s.replace('F', '0')
        s = s.replace('B', '1')
        s = s.replace('L', '0')
        s = s.replace('R', '1')
        row = int(s[0:7], 2)
        c = int(s[7:], 2)
        sid = row * 8 + c
        if sid < min_sid:
            min_sid = sid
        if sid > max_sid:
            max_sid = sid
        existing_sids.append(sid)
    for i in range(min_sid+1, max_sid+1):
        if i not in existing_sids:
            return i

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

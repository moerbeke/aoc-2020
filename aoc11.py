#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

day = 11

########################################################################
# Algorithms
########################################################################

from copy import deepcopy
from collections import namedtuple

P = namedtuple('P', ['x', 'y'])

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

_seats = None
N = 0
M = 0

def parse_input(input_str):
    global _seats
    global N
    global M
    _seats = list()
    lines = input_str.split()
    for line in lines:
        s = list()
        _seats.append(s)
        for l in line:
            s.append(l)
    N = len(_seats)
    M = len(_seats[0])

def print_seats(seats):
    p = str()
    for i in range(N):
        p += ''.join(seats[i]) + '\n'
    print(p)

def reset():
    return

def check_adjacent_seats(seats, n, m):
    adjacent_seats = list()
    for i in [n-1, n, n+1]:
        for j in [m-1, m, m+1]:
            if i >= 0 and i < N and j >= 0 and j < M and not (i == n and j == m):
                adjacent_seats.append(seats[i][j])
    return adjacent_seats.count(EMPTY), adjacent_seats.count(OCCUPIED)

def check_visible_seats(seats, n, m):
    empty_seats = 0
    occupied_seats = 0
    delta_i = [-1, -1, -1, 0, 1, 1, 1, 0]
    delta_j = [-1, 0, 1, 1, 1, 0, -1, -1]
    for d in range(len(delta_i)):
        di = delta_i[d]
        dj = delta_j[d]
        i = n + di
        j = m + dj
        while (i >= 0 and j >= 0 and i < N and j < M):
            p = seats[i][j]
            if p == EMPTY:
                empty_seats += 1
                break
            elif p == OCCUPIED:
                occupied_seats += 1
                break
            i += di
            j += dj
    return empty_seats, occupied_seats

def change_seats(seats):
    new_seats = list()
    for i in range(N):
        new_seats.append(list())
        for j in range(M):
            empty_seats_around, occupied_seats_around = check_adjacent_seats(seats, i, j)
            if seats[i][j] == EMPTY and occupied_seats_around == 0:
                new_seats[i].append(OCCUPIED)
            elif seats[i][j] == OCCUPIED and occupied_seats_around >= 4:
                new_seats[i].append(EMPTY)
            else:
                new_seats[i].append(seats[i][j])
    return new_seats

def change_seats_2(seats):
    new_seats = list()
    for i in range(N):
        new_seats.append(list())
        for j in range(M):
            empty_seats_around, occupied_seats_around = check_visible_seats(seats, i, j)
            if seats[i][j] == EMPTY and occupied_seats_around == 0:
                new_seats[i].append(OCCUPIED)
            elif seats[i][j] == OCCUPIED and occupied_seats_around >= 5:
                new_seats[i].append(EMPTY)
            else:
                new_seats[i].append(seats[i][j])
    return new_seats

def is_chaos(seats1, seats2):
    for i in range(N):
        for j in range(M):
            if seats1[i][j] != seats2[i][j]:
                return True
    return False

def solve_1():
    global _seats
    chaos = True
    print_seats(_seats)
    while chaos:
        print_seats(_seats)
        new_seats = change_seats(_seats)
        chaos = is_chaos(new_seats, _seats)
        if chaos:
            _seats = deepcopy(new_seats)
    print_seats(_seats)
    return sum([line.count(OCCUPIED) for line in _seats])

def solve_2():
    global _seats
    chaos = True
    print_seats(_seats)
    while chaos:
        print_seats(_seats)
        new_seats = change_seats_2(_seats)
        chaos = is_chaos(new_seats, _seats)
        if chaos:
            _seats = deepcopy(new_seats)
    print_seats(_seats)
    return sum([line.count(OCCUPIED) for line in _seats])

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

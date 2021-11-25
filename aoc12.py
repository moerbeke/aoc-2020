#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

day = 12

########################################################################
# Algorithms
########################################################################

EAST = 'E'
WEST = 'W'
NORTH = 'N'
SOUTH = 'S'

_actions = []

class Ship:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._heading = 0

    def do_action(self, action):
        ''' Action N means to move north by the given value.
        Action S means to move south by the given value.
        Action E means to move east by the given value.
        Action W means to move west by the given value.
        Action L means to turn left the given number of degrees.
        Action R means to turn right the given number of degrees.
        Action F means to move forward by the given value in the direction the ship is currently facing.
        '''
        a = action[0]
        n = int(action[1:])
        if a == 'N':
            self._move(NORTH, n)
        elif a == 'S':
            self._move(SOUTH, n)
        elif a == 'E':
            self._move(EAST, n)
        elif a == 'W':
            self._move(WEST, n)
        elif a == 'L':
            self._turn(n)
        elif a == 'R':
            self._turn(-n)
        elif a == 'F':
            self._move(self._my_direction(), n)
        else:
            assert(false)
        #print(action, ' -> ', self._x, self._y, self._heading)

    def _move(self, direction, distance):
        if direction == NORTH:
            self._y += distance
        elif direction == SOUTH:
            self._y -= distance
        elif direction == EAST:
            self._x += distance
        elif direction == WEST:
            self._x -= distance
        else:
            assert(false)

    def _turn(self, degrees):
        self._heading = (self._heading + degrees) % 360

    def _my_direction(self):
        return {0: EAST,
                90: NORTH,
                180: WEST,
                270: SOUTH}[self._heading]

    def get_distance_to_origin(self):
        return abs(self._x) + abs(self._y)

class Ship2:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._wpx = 10
        self._wpy = 1

    def do_action(self, action):
        ''' Action N means to move the waypoint north by the given value.
        Action S means to move the waypoint south by the given value.
        Action E means to move the waypoint east by the given value.
        Action W means to move the waypoint west by the given value.
        Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
        Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        Action F means to move forward to the waypoint a number of times equal to the given value.
        '''
        a = action[0]
        n = int(action[1:])
        if a == 'N':
            self._move_wp(NORTH, n)
        elif a == 'S':
            self._move_wp(SOUTH, n)
        elif a == 'E':
            self._move_wp(EAST, n)
        elif a == 'W':
            self._move_wp(WEST, n)
        elif a == 'L':
            self._turn_wp(n)
        elif a == 'R':
            self._turn_wp(-n)
        elif a == 'F':
            self._move_forward(n)
        else:
            assert(false)
        #print(action, ' -> ', self._x, self._y, self._heading)

    def _move_wp(self, direction, distance):
        if direction == NORTH:
            self._wpy += distance
        elif direction == SOUTH:
            self._wpy -= distance
        elif direction == EAST:
            self._wpx += distance
        elif direction == WEST:
            self._wpx -= distance
        else:
            assert(false)

    def _turn_wp(self, degrees):
        degrees %= 360
        wp0x, wp0y = self._wpx, self._wpy
        if degrees == 90:
            self._wpx = -wp0y
            self._wpy = +wp0x
        elif degrees == 180:
            self._wpx = -wp0x
            self._wpy = -wp0y
        elif degrees == 270:
            self._wpx = +wp0y
            self._wpy = -wp0x
        else:
            assert(false)

    def _move_forward(self, n):
        self._x += self._wpx * n
        self._y += self._wpy * n

    def get_distance_to_origin(self):
        return abs(self._x) + abs(self._y)

def parse_input(input_str):
    global _actions
    _actions = input_str.split('\n')
    _actions = [a for a in _actions if len(a.strip()) > 0]

def reset():
    return

def solve_1():
    ship = Ship()
    for action in _actions:
        ship.do_action(action)
    return ship.get_distance_to_origin()

def solve_2():
    ship = Ship2()
    for action in _actions:
        ship.do_action(action)
    return ship.get_distance_to_origin()

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

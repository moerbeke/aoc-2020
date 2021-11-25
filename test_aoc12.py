#!/usr/bin/env python3

########################################################################
# The Advent of Code 2020
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

import unittest

import testbase
import aocsolver
import aoc12 as aoc

########################################################################
# Test class
########################################################################

class TestAoc12(unittest.TestCase):

    def setUp(self):
        self.aocsolver = aocsolver.AocSolver(aoc.day, aoc.parse_input, aoc.solve_1, aoc.solve_2)
        self.tc_1 = [
                (
"""
F10
N3
F7
R90
F11
""", 25),
                ]
        self.tc_2 = [
                (
"""
F10
N3
F7
R90
F11
""", 286),
                ]

    def tearDown(self):
        pass

    def test_solve_1(self):
        for t in self.tc_1:
            self.assertEqual(self.aocsolver.solve_1(t[0]), t[1])

    def test_solve_2(self):
        for t in self.tc_2:
            self.assertEqual(self.aocsolver.solve_2(t[0]), t[1])


########################################################################
# Main program
########################################################################

if __name__ == '__main__':
    testbase.run_test(TestAoc12)

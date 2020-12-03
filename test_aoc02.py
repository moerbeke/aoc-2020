#!/usr/bin/env python3

########################################################################
# The Advent of Code 2020
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

import unittest

import testbase
import aocsolver
import aoc02 as aoc

########################################################################
# Test class
########################################################################

class TestAoc02(unittest.TestCase):

    def setUp(self):
        self.aocsolver = aocsolver.AocSolver(aoc.day, aoc.parse_input, aoc.solve_1, aoc.solve_2)
        self.tc_1 = [
                (
"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""", 2),
                ]
        self.tc_2 = [
                (
"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""", 1),
                (
"""
1-3 a: abcde
1-3 a: Xbade
1-3 b: cdefg
2-9 c: ccccccccc
""", 2),
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
    testbase.run_test(TestAoc02)

#!/usr/bin/env python3

########################################################################
# The Advent of Code 2021
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

import unittest

import testbase
import aocsolver
import aoc09 as aoc

########################################################################
# Test class
########################################################################

class TestAoc09(unittest.TestCase):

    def setUp(self):
        self.aocsolver = aocsolver.AocSolver(aoc.day, aoc.parse_input, aoc.solve_1, aoc.solve_2)
        self.tc_1 = [
                (
"""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""", 127),
                ]
        self.tc_2 = [
                (
"""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""", 62),
                ]

    def tearDown(self):
        pass

    def test_solve_1(self):
        aoc.set_preamble(5)
        for t in self.tc_1:
            self.assertEqual(self.aocsolver.solve_1(t[0]), t[1])

    def test_solve_2(self):
        aoc.set_preamble(5)
        for t in self.tc_2:
            self.assertEqual(self.aocsolver.solve_2(t[0]), t[1])


########################################################################
# Main program
########################################################################

if __name__ == '__main__':
    testbase.run_test(TestAoc09)

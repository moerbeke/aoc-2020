#!/usr/bin/env python3

########################################################################
# The Advent of Code 2021
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

import unittest

import testbase
import aocsolver
import aoc08 as aoc

########################################################################
# Test class
########################################################################

class TestAoc08(unittest.TestCase):

    def setUp(self):
        self.aocsolver = aocsolver.AocSolver(aoc.day, aoc.parse_input, aoc.solve_1, aoc.solve_2)
        self.tc_1 = [
                (
"""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""", 5),
                ]
        self.tc_2 = [
                (
"""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""", 8),
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
    testbase.run_test(TestAoc08)

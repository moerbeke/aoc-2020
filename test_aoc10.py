#!/usr/bin/env python3

########################################################################
# The Advent of Code 2021
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

import unittest

import testbase
import aocsolver
import aoc10 as aoc

########################################################################
# Test class
########################################################################

class TestAoc10(unittest.TestCase):

    def setUp(self):
        self.aocsolver = aocsolver.AocSolver(aoc.day, aoc.parse_input, aoc.solve_1, aoc.solve_2)
        self.tc_1 = [
                (
"""
16
10
15
5
1
11
7
19
6
12
4
""", 7*5),
                (
"""
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""", 22*10),
                ]
        self.tc_2 = [
                (
"""
16
10
15
5
1
11
7
19
6
12
4
""", 8),
                (
"""
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""", 19208),
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
    testbase.run_test(TestAoc10)

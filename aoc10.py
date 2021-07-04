#!/usr/bin/env python3

########################################################################
# Advent of Code 2021 - solver
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

day = 10

'''Notes

Part 1 - result:
    number of 1-jolt differences multiplied by the number of 3-jolt differences

Puzzle input:
    List of output joltage ratings of the adapters

Any adapter can take an input 1, 2 or 3 jolts lower than its rating and still produce its rated output joltage.
In addition, there is a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter.

Charging outlet effective joltage rating = 0
'''

########################################################################
# Algorithms
########################################################################

from itertools import combinations

_ratings = None

def parse_input(input_str):
    global _ratings
    _ratings = [int(line) for line in input_str.strip().split('\n')]

def solve_1():
    count_1 = 0
    count_3 = 0
    adapters = sorted(_ratings)
    adapters.append(max(adapters) + 3)
    prev_joltage = 0
    for joltage in adapters:
        assert(joltage > prev_joltage and joltage <= prev_joltage + 3)
        if joltage - prev_joltage == 1:
            count_1 += 1
        elif joltage - prev_joltage == 3:
            count_3 += 1
        prev_joltage = joltage
    return count_1 * count_3

def count_arrangements(chain):
    arrangements = list()
    assert(len(chain) > 0)
    arrangements.append(chain)
    if len(chain) > 2:
        first = chain[0]
        last = chain[-1]
        arrangements.append([first, last])
        midchain = chain[1:-1]
        for n in range(1, len(midchain)):
            subchains = [list(c) for c in combinations(midchain, n)]
            for subchain in subchains:
                subchain.insert(0, first)
                subchain.append(last)
                arrangements.append(subchain)
    n_arrangements = 0
    for arrangement in arrangements:
        delta = list()
        for j in range(1, len(arrangement)):
            delta.append(arrangement[j] - arrangement[j-1])
        if len(delta) == 0 or max(delta) <= 3:
            n_arrangements += 1
    return n_arrangements

def solve_2():
    global _adapters
    adapters = sorted(_ratings)
    # Split into chains of adapters, so that chains are separated from each other by 3 jolts.
    chains = list()
    chain = list()
    chains.append(chain)
    chain.append(0)
    prev_joltage = 0
    for joltage in adapters:
        assert(joltage > prev_joltage and joltage <= prev_joltage + 3)
        if joltage - prev_joltage < 3:
            chain.append(joltage)
        else:
            chain = list()
            chain.append(joltage)
            chains.append(chain)
        prev_joltage = joltage
    # Count number of arrangements for each chain, and multiply them
    n_arrangements = 1
    for chain in chains:
        n_arrangements *= count_arrangements(chain)
    return n_arrangements

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

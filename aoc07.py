#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 7

########################################################################
# Algorithms
########################################################################

_target = 'shiny gold'
_level = 0

def parse_input(input_str):
    '''
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    faded blue bags contain no other bags.
    '''
    global _rules
    global _bags
    global _bags_count
    _rules = input_str.strip().split('\n')
    _bags = dict()
    _bags_count = dict()
    for r in _rules:
        container_color, contents = r.split('bags contain')
        container_bag = container_color.split('bags')[0].strip()
        container_color = container_color.strip()
        _bags[container_color] = set()
        _bags_count[container_color] = list()
        if 'no other' not in contents:
            for c in contents.split(','):
                c = c.strip().split(' ')
                bag = c[1] + ' ' + c[2]
                _bags[container_color].add(bag)
                _bags_count[container_color].extend([bag]* int(c[0]))

def reset():
    return

def solve_1():
    contain_shiny_gold = 0
    for c in _bags:
        if search_contents_for(c, _target):
            contain_shiny_gold += 1
    return contain_shiny_gold

def solve_2():
    global _n_bags
    _n_bags = 0
    count_bags_inside(_target)
    return _n_bags

def search_contents_for(color, target):
    global _level
    found = False
    if target in _bags[color]:
        found = True
    else:
        for c in _bags[color]:
            if c in _bags:
                _level += 1
                found = search_contents_for(c, target)
                _level -= 1
                if found:
                    break
    return found

def count_bags_inside(color):
    global _n_bags
    if color in _bags_count:
        bags_inside_color = _bags_count[color]
        _n_bags += len(bags_inside_color)
        for c in bags_inside_color:
            count_bags_inside(c)

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

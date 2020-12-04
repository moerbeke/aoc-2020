#!/usr/bin/env python3

########################################################################
# Advent of Code 2020 - solver
#
# Copyright (C) 2020 Antonio Ceballos Roa
########################################################################

day = 4

########################################################################
# Algorithms
########################################################################

'''passport fields
cid is optional

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

passport_required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parse_input(input_str):
    global _passports
    _passports = list()
    blocks = [p for p in input_str.strip().split('\n\n')]
    for b in blocks:
        fields = b.strip().replace('\n', ' ').split(' ')
        if len(fields) > 0:
            _passports.append(fields)

def reset():
    return

def solve_1():
    n_valid_passports = 0
    for p in _passports:
        n = 0
        for f in p:
            fid = f.split(':')[0]
            if fid in passport_required_fields:
                n += 1
        if n >= 7:
            n_valid_passports += 1
    return n_valid_passports

def solve_2():
    n_valid_passports = 0
    for p in _passports:
        n = 0
        for f in p:
            if is_valid(f):
                n += 1
        if n >= 7:
            n_valid_passports += 1
    return n_valid_passports

def is_valid(field):
    ''' Validity rules:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    fid, fval = field.strip().split(':')
    valid = False
    if fid == 'byr':
        val = int(fval)
        valid = (val >= 1920 and val <= 2002)
    elif fid == 'iyr':
        val = int(fval)
        valid = (val >= 2010 and val <= 2020)
    elif fid == 'eyr':
        val = int(fval)
        valid = (val >= 2020 and val <= 2030)
    elif fid == 'hgt':
        if 'cm' in fval:
            val = int(fval[:-2])
            valid = (val >= 150 and val <= 193)
        elif 'in' in fval:
            val = int(fval[:-2])
            valid = (val >= 59 and val <= 76)
    elif fid == 'hcl':
        if len(fval) == 7 and fval[0] == '#':
            codes = '0123456789abcdef'
            invalid = False
            for c in fval[1:]:
                if c not in codes:
                    invalid = True
                    break
            valid = not invalid
    elif fid == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = fval in colors
    elif fid == 'pid':
        if len(fval) == 9:
            valid = (int(fval) >= 0)
    return valid

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

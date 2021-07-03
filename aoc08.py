#!/usr/bin/env python3

########################################################################
# Advent of Code 2021 - solver
#
# Copyright (C) 2021 Antonio Ceballos Roa
########################################################################

day = 8

########################################################################
# Algorithms
########################################################################

class Inst:

    def __init__(self, pos, inst_str):
        self._pos = pos
        self._parse_inst(inst_str)
        self._exec_count = 0

    def _parse_inst(self, inst_str):
        op, arg_str = inst_str.split(' ')
        assert(arg_str[0] == '+' or arg_str[0] == '-')
        s = 1 if arg_str[0] == '+' else -1
        n = int(arg_str[1:])
        arg = s * n
        self._op = op
        self._arg = arg

    def inc_exec(self):
        self._exec_count += 1

    def reset(self):
        self._exec_count = 0

    def fix(self, op):
        self._op = op

    @property
    def exec_count(self):
        return self._exec_count

    @property
    def op(self):
        return self._op

    @property
    def arg(self):
        return self._arg

def parse_input(input_str):
    '''
    Examples of instructions:
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    '''
    global _instructions
    _instructions = list()
    instructions_str = input_str.strip().split('\n')
    pos = 0
    for inst_str in instructions_str:
        _instructions.append(Inst(pos, inst_str))
        pos += 1

def reset():
    return

def run_program():
    acc = 0
    pos = 0
    prog_len = len(_instructions)
    inst = _instructions[pos]
    while inst.exec_count == 0:
        if inst.op == 'acc':
            acc += inst.arg
            pos = pos + 1
        elif inst.op == 'nop':
            pos = pos + 1
        elif inst.op == 'jmp':
            pos = pos + inst.arg
        else:
            assert(False)
        inst.inc_exec()
        assert(pos < prog_len)
        inst = _instructions[pos]
    return acc

def run_program_exit():
    for inst in _instructions:
        inst.reset()
    acc = 0
    pos = 0
    prog_len = len(_instructions)
    inst = _instructions[pos]
    success = False
    while inst.exec_count == 0:
        inst.inc_exec()
        if inst.op == 'acc':
            acc += inst.arg
            pos = pos + 1
        elif inst.op == 'nop':
            pos = pos + 1
        elif inst.op == 'jmp':
            pos = pos + inst.arg
        else:
            assert(False)
        if pos == prog_len:
            success = True
            break
        else:
            assert(pos < prog_len)
            inst = _instructions[pos]
    return acc, success

def solve_1():
    acc = run_program()
    return acc

def solve_2():
    prog_len = len(_instructions)
    for pos in range(prog_len):
        orig_op = _instructions[pos].op
        if orig_op == 'nop':
            fix_op = 'jmp'
        elif orig_op == 'jmp':
            fix_op = 'nop'
        else:
            continue
        _instructions[pos].fix(fix_op)
        acc, success = run_program_exit()
        _instructions[pos].fix(orig_op)
        if success:
            break
    assert(success)
    return acc

########################################################################
# main
########################################################################

if __name__ == '__main__':
    import aocsolver
    aocsolver.AocSolver(day, parse_input, solve_1, solve_2).run()

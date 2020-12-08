#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Computer:
    def __init__(self, program, acc_val=0, index=0):
        self.program = program
        self.program_length = len(self.program)
        self.acc_val = acc_val
        self.index = index
        self.iterations = 0

    def run_until_repeat(self):
        run_indexes = []
        while self.index not in run_indexes:
            run_indexes.append(self.index)
            op, val = self.decode_op(self.program[self.index])
            op_method = getattr(self, op)
            op_method(val)
        return self.acc_val

    def run_until_complete(self):
        run_indexes = []
        while self.index not in run_indexes:
            old_index = self.index
            run_indexes.append(self.index)
            op, val = self.decode_op(self.program[self.index])
            op_method = getattr(self, op)
            op_method(val)
            if old_index == self.program_length - 1:
                return self.acc_val
        return None

    def decode_op(self, op_str):
        op, mod = op_str.split(" ")
        return op, int(mod)

    def acc(self, val):
        self.acc_val += val
        self.index = (self.index + 1) % self.program_length

    def nop(self, val):
        self.index = (self.index + 1) % self.program_length

    def jmp(self, val):
        self.index = (self.index + val) % self.program_length


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        comp = Computer(inp)
        acc_val = comp.run_until_repeat()
        return acc_val


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        ops = [inst.split(" ")[0] for inst in inp]
        nops = [index for index, op in enumerate(ops) if op == "nop"]
        jmps = [index for index, op in enumerate(ops) if op == "jmp"]
        for nop_index in nops:
            inp[nop_index] = inp[nop_index].replace("nop", "jmp")
            comp = Computer(inp)
            acc_val = comp.run_until_complete()
            if acc_val is not None:
                return acc_val
            inp[nop_index] = inp[nop_index].replace("jmp", "nop")

        for jmp_index in jmps:
            inp[jmp_index] = inp[jmp_index].replace("jmp", "nop")
            comp = Computer(inp)
            acc_val = comp.run_until_complete()
            if acc_val is not None:
                return acc_val
            inp[jmp_index] = inp[jmp_index].replace("nop", "jmp")


if __name__ == "__main__":
    day_number = 8
    test_input = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=5,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=8,
    )
    part_2.submit_answer()

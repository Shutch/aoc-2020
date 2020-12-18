#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        equations = []
        equation = ""
        for line in inp:
            equation = equation + line
            if line[-1] != " ":
                equations.append(equation)
                equation = ""

        for equation in equations:
            # checking for parenthesis
            open_parenthesis = []
            parenthesis = []
            for index, letter in enumerate(equation):
                if letter == "(":
                    open_parenthesis.append(index)
                elif letter == ")":
                    parenthesis.append()


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


if __name__ == "__main__":
    day_number = 18
    test_input = [
        "2 * 3 + ",
        "(4 * 5)",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=26,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=0,
    )
    part_2.submit_answer()

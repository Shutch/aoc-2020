#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging
from operator import mul, add
import re

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

        equation_values = []
        for equation in equations:
            while "(" in equation:
                equation = compute_deepest_parenthesis(equation)

            # final computation with no parenthesis
            equation = compute_equation(equation)
            equation_values.append(int(equation))
        return sum(equation_values)


def compute_deepest_parenthesis(equation):
    level = 0
    max_level = level
    max_open_index = None
    simplified_equation = equation
    for index, char in enumerate(equation):
        if char == "(":
            level += 1
            if level > max_level:
                max_level = level
                max_open_index = index
        elif char == ")":
            level -= 1
            if level == (max_level - 1):
                max_close_index = index
                break
    if max_open_index is not None:
        sub_eq = equation[max_open_index + 1 : max_close_index]
        computed_parenthesis = compute_equation(sub_eq)
        simplified_equation = (
            equation[:max_open_index]
            + computed_parenthesis
            + equation[max_close_index + 1 :]
        )
        # logger.debug(f"Simplified equation: {simplified_equation}")

    return simplified_equation


def compute_equation(equation):
    # no parenthesis allowed
    equation = equation.split(" ")
    # compute addition first
    while "+" in equation:
        add_index = equation.index("+")
        new_value = int(equation[add_index - 1]) + int(equation[add_index + 1])
        equation[add_index] = new_value
        del equation[add_index + 1]
        del equation[add_index - 1]

    while "*" in equation:
        mult_index = equation.index("*")
        new_value = int(equation[mult_index - 1]) * int(equation[mult_index + 1])
        equation[mult_index] = new_value
        del equation[mult_index + 1]
        del equation[mult_index - 1]
    return str(equation[0])


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        equations = []
        equation = ""
        for line in inp:
            equation = equation + line
            if line[-1] != " ":
                equations.append(equation)
                equation = ""

        equation_values = []
        for equation in equations:
            while "(" in equation:
                equation = compute_deepest_parenthesis(equation)

            # final computation with no parenthesis
            equation = compute_equation(equation)
            equation_values.append(int(equation))
        return sum(equation_values)


if __name__ == "__main__":
    day_number = 18
    test_input = [
        "(2 * 3) + ",
        "(4 * 5 * (1 * 1))",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=26,
    )
    part_1.submit_answer()

    test_input = [
        "((2 + 4 * 9) * ",
        "(6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=23340,
    )
    part_2.submit_answer()

#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


if __name__ == "__main__":
    day_number = 0
    test_input = []

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=0,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=0,
    )
    part_2.submit_answer()

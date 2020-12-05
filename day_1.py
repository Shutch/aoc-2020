#!/usr/bin/env python
# mypy: ignore-errors
import aoc


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        inp = [int(val) for val in inp]
        for a in inp:
            for b in inp:
                if (a + b) == 2020:
                    return a * b


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        inp = [int(val) for val in inp]
        for a in inp:
            for b in inp:
                for c in inp:
                    if (a + b + c) == 2020:
                        return a * b * c


if __name__ == "__main__":
    day_number = 1
    test_input = ["1721", "979", "366", "299", "675", "1456"]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=514579,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=241861950,
    )
    part_2.submit_answer()

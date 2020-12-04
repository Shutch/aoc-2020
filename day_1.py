#!/usr/bin/env python
# mypy: ignore-errors
import aoc


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        inp = aoc.convert_str_list(inp, int)
        for a in inp:
            for b in inp:
                if (a * b) == 2020:
                    return a * b


if __name__ == "__main__":
    puzzle_input: List[str] = aoc.get_input(1)
    part_1 = Part1(
        day_number=1,
        test_input=["1721", "979", "366", "299", "675", "1456"],
        test_answer=514579,
        real_input=puzzle_input,
    )
    part_1.test()

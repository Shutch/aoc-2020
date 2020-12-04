#!/usr/bin/env python
# mypy: ignore-errors
import aoc


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        valid_passwords = 0
        for line in inp:
            if line != "":
                parts = line.split()
                low, high = parts[0].split("-")
                letter = parts[1].strip(":")
                pw = parts[2]
                if pw.count(letter) >= int(low) and pw.count(letter) <= int(high):
                    valid_passwords += 1
        return valid_passwords


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


if __name__ == "__main__":
    day_number = 2
    test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=2,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=0,
    )
    part_2.submit_answer()

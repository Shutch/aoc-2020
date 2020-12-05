#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        trees = 0
        right_jump = 3
        down_jump = 1
        x = 0  # Top left corner, right is +x, down is y+
        width = len(inp[0])
        for y, line in enumerate(inp):
            if y % down_jump == 0:
                char = line[x % width]
                if char == "#":
                    trees += 1
                x += right_jump
        return trees


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        total_trees = 1
        for case in cases:
            trees = 0
            right_jump = case[0]
            down_jump = case[1]
            x = 0  # Top left corner, right is +x, down is y+
            width = len(inp[0])
            for y, line in enumerate(inp):
                if y % down_jump == 0:
                    char = line[x % width]
                    if char == "#":
                        trees += 1
                    x += right_jump
            total_trees = total_trees * trees
        return total_trees


if __name__ == "__main__":
    day_number = 3
    test_input = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=7,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=336,
    )
    part_2.submit_answer()

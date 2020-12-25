#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        public_keys = [int(inp[0]), int(inp[1])]

        subject_number = 7
        loop_sizes = []
        for key in public_keys:
            loop_size = 0
            value = 1
            while value != key:
                value = value * subject_number
                value = value % 20201227
                loop_size += 1
            loop_sizes.append(loop_size)
        logger.debug(loop_sizes)

        # getting the private encryption key from the first public key
        subject_number = public_keys[1]
        value = 1
        for i in range(loop_sizes[0]):
            value = value * subject_number
            value = value % 20201227
        logger.debug(value)

        return value


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


if __name__ == "__main__":
    day_number = 25
    test_input = [
        "5764801",
        "17807724",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=14897079,
    )
    part_1.submit_answer()

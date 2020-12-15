#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        spoken_numbers = [int(line) for line in inp[0].split(",")[::-1]]  # reverse ord
        # logger.debug(f"Input numbers: {spoken_numbers}")
        while len(spoken_numbers) < 2020:
            try:
                last_number = spoken_numbers[0]
                previous_turn = len(spoken_numbers) - spoken_numbers.index(
                    last_number, 1
                )
                last_turn_number = len(spoken_numbers)
                spoken_numbers.insert(0, last_turn_number - previous_turn)
                # logger.debug(f"Repeat: {last_number}: {last_turn_number} - {previous_turn}")
            except ValueError:
                # logger.debug(f"Unique: {spoken_numbers[0]}")
                spoken_numbers.insert(0, 0)

        # logger.debug(f"Last numbers: {spoken_numbers[:10]}")
        return spoken_numbers[0]


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        split_input = [int(val) for val in inp[0].split(",")]
        spoken_numbers = {value: (index + 1) for index, value in enumerate(split_input)}
        last_occurence = None
        last_number = split_input[-1]
        # logger.debug(f"Input numbers: {spoken_numbers}")
        current_turn = len(spoken_numbers)
        while current_turn < 30000000:
            current_turn += 1
            if last_occurence is None:
                last_number = 0
                last_occurence = spoken_numbers.get(0, None)
                spoken_numbers[0] = current_turn
            else:
                next_number = current_turn - last_occurence - 1
                last_occurence = spoken_numbers.get(next_number, None)
                spoken_numbers[next_number] = current_turn
                last_number = next_number
            # logger.debug(f"Spoken: {last_number}")
        return last_number


if __name__ == "__main__":
    day_number = 15
    test_input = ["0,3,6"]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=436,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=175594,
    )
    part_2.submit_answer()

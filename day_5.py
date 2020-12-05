#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        max_id = 0
        for boarding_pass in inp:
            row_bin = boarding_pass[:7].replace("B", "1").replace("F", "0")
            row = int(row_bin, 2)
            column_bin = boarding_pass[7:].replace("R", "1").replace("L", "0")
            column = int(column_bin, 2)
            seat_id = row * 8 + column
            if seat_id > max_id:
                max_id = seat_id
        return max_id


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        seat_ids = []
        for boarding_pass in inp:
            row_bin = boarding_pass[:7].replace("B", "1").replace("F", "0")
            row = int(row_bin, 2)
            column_bin = boarding_pass[7:].replace("R", "1").replace("L", "0")
            column = int(column_bin, 2)
            seat_id = row * 8 + column
            seat_ids.append(seat_id)
        list.sort(seat_ids)
        first_seat_id = seat_ids[0]
        last_seat_id = seat_ids[-1]
        full_id_set = list(range(first_seat_id, last_seat_id + 1))
        missing_id = sum(full_id_set) - sum(seat_ids)
        return missing_id


if __name__ == "__main__":
    day_number = 5
    test_input = [
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=820,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=327726,  # No test case for this part
    )
    part_2.submit_answer()

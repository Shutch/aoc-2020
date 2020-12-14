#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        start_time = int(inp[0])
        bus_ids = []
        for bus_id in inp[1].split(","):
            if bus_id != "x":
                bus_ids.append(int(bus_id))
        current_time = start_time
        while True:
            for bus_id in bus_ids:
                if current_time % bus_id == 0:
                    return (current_time - start_time) * bus_id
            current_time += 1


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        busses = {}
        for time, bus_id in enumerate(inp[1].split(",")):
            if bus_id != "x":
                busses[int(bus_id)] = int(time)

        # 0 sorts by id, 1 sorts by time from t
        busses = {
            key: value
            for key, value in sorted(
                busses.items(), key=lambda item: item[0], reverse=True
            )
        }
        main_id = max(busses)
        main_offset = busses[main_id]
        current_time = main_id
        while True:
            # cycle through busses, check modulo == 0, if not then break
            passes = True
            for bus_id, offset in busses.items():
                if (current_time + (offset - main_offset)) % bus_id != 0:
                    passes = False
                    break
            if passes:
                return current_time - main_offset
            current_time += main_id


if __name__ == "__main__":
    day_number = 13
    test_input = [
        "939",
        "7,13,x,x,59,x,31,19",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=295,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=1068781,
    )
    part_2.submit_answer()

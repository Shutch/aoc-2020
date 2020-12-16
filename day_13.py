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
        # Setting offset relative to the last bus
        latest_bus_offset = max(list(busses.values()))
        busses = {
            key: latest_bus_offset - value
            for key, value in sorted(
                busses.items(), key=lambda item: item[0], reverse=True
            )
        }
        logger.debug(busses)

        # starting with the largest ID (largest modulus), iterate along all values that
        # satisfy first_offset = value % first_ID. When a value is equal to
        # second_offset = value % second_ID, now iterate first_ID * second_ID.
        # repeat this process until all congruences are satisfied
        # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
        jump_size = max(busses)
        current_value = busses[jump_size]
        for bus_id, offset in list(busses.items())[1:]:
            logger.debug(
                f"New bus: {bus_id}, offset:{offset}. Current Value: {current_value}. Jump Size: {jump_size}"
            )
            while (current_value % bus_id) != (offset % bus_id):
                current_value += jump_size
            jump_size = jump_size * bus_id

        final_time = current_value - latest_bus_offset
        logger.debug(f"Final value: {final_time}, Jump size: {jump_size}")
        return final_time


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

    test_input = ["939", "7,13,x,x,59,x,31,19"]
    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=1068781,
    )
    part_2.submit_answer()

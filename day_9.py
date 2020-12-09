#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


def find_components(pool, target_val):
    for i in pool:
        for j in pool:
            if i != j and i + j == target_val:
                return True
    return False


def find_sum(pool, starting_index, target_val):
    contigous_sum = 0
    for i, val in enumerate(pool[starting_index:]):
        contigous_sum += val
        if contigous_sum > target_val:
            return 0
        elif contigous_sum == target_val:
            return i
    return 0


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        # weird fix for test preamble size vs full preamble size
        if type(inp) == dict:
            preamble_size = inp["preamble"]
            inp = inp["inp"]
        else:
            preamble_size = 25

        inp = [int(val) for val in inp]
        for index, val in enumerate(inp[preamble_size:]):
            components_found = find_components(inp[index : preamble_size + index], val)
            if components_found is False:
                return val


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        # weird fix for test preamble size vs full preamble size
        if type(inp) == dict:
            preamble_size = inp["preamble"]
            inp = inp["inp"]
        else:
            preamble_size = 25

        inp = [int(val) for val in inp]
        for index, val in enumerate(inp[preamble_size:]):
            components_found = find_components(inp[index : preamble_size + index], val)
            if components_found is False:
                target_val = val
                break

        for i, val_1 in enumerate(inp):
            contigous_length = find_sum(inp, i, target_val)
            if contigous_length > 0:
                contigous_span = inp[i : i + contigous_length + 1]
                return min(contigous_span) + max(contigous_span)


if __name__ == "__main__":
    day_number = 9
    test_input = {
        "preamble": 5,
        "inp": [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576",
        ],
    }

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=127,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=62,
    )
    part_2.submit_answer()

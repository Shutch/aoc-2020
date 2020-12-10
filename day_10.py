#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging
from collections import defaultdict

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        inp = [int(val) for val in inp]
        inp.sort()
        lower_rating = 0
        one_ratings = 0
        three_ratings = 0
        for charger_rating in inp:
            if charger_rating - lower_rating == 1:
                one_ratings += 1
            if charger_rating - lower_rating == 2:
                pass
            if charger_rating - lower_rating == 3:
                three_ratings += 1
            lower_rating = charger_rating
        three_ratings += 1
        return one_ratings * three_ratings


def find_combinations(inp):
    combinations = {}
    total_chargers = len(inp)
    i = 0
    j = 1
    while i < total_chargers:
        charger_rating = inp[i]
        combinations[charger_rating] = []
        j = i + 1
        if j < total_chargers:
            next_charger = inp[j]
            while next_charger - charger_rating <= 3 and j < total_chargers:
                combinations[charger_rating].append(next_charger)
                j += 1
                if j >= total_chargers:
                    break
                next_charger = inp[j]
        i += 1
    return combinations


def find_paths(combinations, current_charger, final_charger, total_paths):
    paths = combinations[current_charger]
    if current_charger == final_charger:
        return total_paths + 1
    elif current_charger < final_charger:
        for path in paths:
            if path <= final_charger:
                total_paths = find_paths(combinations, path, final_charger, total_paths)
    return total_paths


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        inp = [int(val) for val in inp]
        inp.sort()
        first_charger = 0
        final_charger = max(inp) + 3
        inp.insert(0, first_charger)
        inp.append(final_charger)
        combinations = find_combinations(inp)
        # splitting graph into subgraphs by nodes with one path through them
        single_nodes = [val[0] for key, val in combinations.items() if len(val) == 1]
        single_nodes.insert(0, first_charger)
        single_nodes.append(final_charger)
        total_paths = 1
        for index, value in enumerate(single_nodes[:-1]):
            start_node = value
            end_node = single_nodes[index + 1]
            new_paths = find_paths(combinations, start_node, end_node, 0)
            total_paths = new_paths * total_paths
        return total_paths


if __name__ == "__main__":
    day_number = 10
    test_input = [
        "28",
        "33",
        "18",
        "42",
        "31",
        "14",
        "46",
        "20",
        "48",
        "47",
        "24",
        "23",
        "49",
        "45",
        "19",
        "38",
        "39",
        "11",
        "1",
        "32",
        "25",
        "35",
        "8",
        "17",
        "7",
        "9",
        "4",
        "2",
        "34",
        "10",
        "3",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=22 * 10,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=19208,
    )
    part_2.submit_answer()

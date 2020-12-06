#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        inp.append("")
        group = ""
        total_answers = 0
        for line in inp:
            if line == "":
                total_answers += len(set(group))
                group = ""
            else:
                group = group + line
        return total_answers


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        inp.append("")
        group = []
        total_answers = 0
        for line in inp:
            if line == "":
                not_answered = []
                all_answers = list(set("".join(group)))
                for person in group:
                    for answer in all_answers:
                        if answer not in person:
                            not_answered.append(answer)
                not_answered = list(set(not_answered))
                answered_answers = set(all_answers).difference(set(not_answered))
                total_answers += len(answered_answers)

                group = []
            else:
                group.append(line)
        return total_answers


if __name__ == "__main__":
    day_number = 6
    test_input = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]
    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=11,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=6,
    )
    part_2.submit_answer()

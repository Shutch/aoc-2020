#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging
from copy import deepcopy

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        line_num = 0
        line = inp[line_num]
        rules = {}
        while line != "":
            rule_num, sub_rules = line.split(": ")
            if sub_rules[1].isalpha():
                sub_rules = [sub_rules[1]]
            else:
                sub_rules = sub_rules.split(" | ")
                sub_rules = [rule.split(" ") for rule in sub_rules]
                sub_rules = [
                    [int(sub_sub_rule) for sub_sub_rule in sub_rule]
                    for sub_rule in sub_rules
                ]
            rules[int(rule_num)] = sub_rules
            line_num += 1
            line = inp[line_num]

        messages = []
        line_num += 1
        for line in inp[line_num:]:
            messages.append(line)

        logger.debug(rules)
        logger.debug(messages)

        possible_messages = []
        message = depth_first_search(rules, 0, "", possible_messages)
        logger.debug(message)
        logger.debug(possible_messages)

        # building valid messages from 0
        # valid_messages = 0
        # for message in messages:
        #     if message in possible_messages:
        #         valid_messages += 1

        # return valid_messages


def depth_first_search(rules, rule_index, starting_message, possible_messages):
    sub_rules = rules[rule_index]
    for sub_rule_index, sub_rule in enumerate(sub_rules):
        current_message = starting_message
        if type(sub_rule) == str:
            logger.debug(f"Current message: {starting_message} + {sub_rule}")
            return starting_message + sub_rule
        else:
            for step_index, step in enumerate(sub_rule):
                current_message = depth_first_search(
                    rules, step, current_message, possible_messages
                )
                logger.debug(
                    f"Rule {rule_index}, Sub-rule {sub_rule_index}, Step {step_index} complete: {step} {current_message}"
                )
        logger.debug(
            f"Rule {rule_index}, Sub-rule {sub_rule_index} complete: {sub_rule} {current_message}"
        )
        possible_messages.append(current_message)
    logger.debug(f"Rule {rule_index} complete: {current_message}")
    return current_message


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        pass


if __name__ == "__main__":
    day_number = 19
    test_input = [
        "0: 4 1 5",
        "1: 2 3 | 3 2",
        "2: 4 4 | 5 5",
        "3: 4 5 | 5 4",
        '4: "a"',
        '5: "b"',
        "",
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]

    test_input = [
        "0: 1 2",
        '1: "a"',
        "2: 1 3 | 3 1",
        '3: "b"',
        "",
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]

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

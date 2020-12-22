#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

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
                sub_rules = sub_rules[1]
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

        # building possible valid messages
        possible_messages = []
        find_possible_messages(rules, 0, "", possible_messages)
        logger.debug(possible_messages)

        valid_messages = 0
        for message in messages:
            if message in possible_messages:
                valid_messages += 1

        return valid_messages


def find_possible_messages(rules, current_rule_id, starting_message, possible_messages):
    logger.debug(f"Sub-rule: {current_rule_id}, message: {starting_message}")
    rule = rules[current_rule_id]
    if type(rule) == str:
        logger.debug(f"Returning {starting_message + rule}")
        return starting_message + rule
    elif type(rule) == list:
        for sub_rule in rule:
            logger.debug(f"New branch starting with {starting_message}")
            current_message = starting_message
            for next_rule_id in sub_rule:
                current_message = find_possible_messages(
                    rules, next_rule_id, current_message, possible_messages
                )
                logger.debug(
                    f"Rule {current_rule_id}, sub rule {sub_rule}, sequence {next_rule_id}, Current message: {current_message}"
                )
    else:
        raise ValueError(f"Unexpected rule value {rule}")
    logger.debug(f"Exiting with message {current_message}")
    return possible_messages


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

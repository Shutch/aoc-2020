#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")
logger.setLevel(logging.DEBUG)


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        line_num = 0
        line = inp[line_num]
        rules = {}
        while line != "":
            rule_num, sub_rules = line.split(": ")
            if sub_rules[1].isalpha():
                sub_rules = [[sub_rules[1]]]
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

        # rules = reverse_simplification(rules)
        possible_messages = depth_first_search(rules)

        # building valid messages from 0
        valid_messages = 0
        for message in messages:
            if message in possible_messages:
                valid_messages += 1

        return valid_messages


# depth first is problematic because as the depth gets deeper, additional paths need to be
# managed for each level e.g. a sub rule at level one can just create and manage an
# additional possible message but a sub rule at level two will need to manage 2 additional
# possible messages and update them accordingly
def depth_first_search(rules, starting_rule_id=0):
    logger.debug("DFS")
    possible_messages = [""]
    rule = rules[starting_rule_id]
    possible_messages = complete_rule(rules, rule, possible_messages.copy())
    logger.debug(f"Complete Rule: {rule} {possible_messages}")
    return possible_messages


def complete_rule(rules, rule, possible_messages):
    logger.debug(f"Enter Rule: {rule} {possible_messages}")
    # the possible messages is multiplied by the number of sub rules
    # 1 message, 1 sub-rule = 1 message, 1 to 1
    # 2 messages, 1 sub-rule = 2 messages, 2 to 1
    # 2 messages, 2 sub_rules = 4 messages, 2 to 2
    original_messages = possible_messages.copy()
    combined_messages = []
    # for message_id in range(len(original_messages)):
    for message_id in range(1):
        for sub_rule_id, sub_rule in enumerate(rule):
            combined_messages = combined_messages + complete_sub_rule(
                rules, sub_rule, original_messages.copy()
            )
            logger.debug(f"Complete Sub-Rule: {sub_rule} {combined_messages}")
    return combined_messages


def complete_sub_rule(rules, sub_rule, possible_messages):
    logger.debug(f"Enter Sub-rule: {sub_rule} {possible_messages}")
    for step in sub_rule:
        possible_messages = complete_step(rules, step, possible_messages.copy())
        logger.debug(f"Complete Step: {step} {possible_messages}")
    return possible_messages


def complete_step(rules, step, possible_messages):
    logger.debug(f"Enter Step: {step} {possible_messages}")
    if type(step) == str:
        for message_id, message in enumerate(possible_messages):
            possible_messages[message_id] = message + step
    else:
        rule = rules[step]
        possible_messages = complete_rule(rules, rule, possible_messages.copy())
        logger.debug(f"Complete Rule: {rule} {possible_messages}")
    return possible_messages


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        line_num = 0
        line = inp[line_num]
        rules = {}
        while line != "":
            rule_num, sub_rules = line.split(": ")
            if sub_rules[1].isalpha():
                sub_rules = [[sub_rules[1]]]
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

        # manual replacement
        rule_8 = []
        rule_11 = []
        for i in range(3):  # this is probably enough
            rule_8.append([42] * (i + 1))
            rule_11.append(([42] * (i + 1)) + ([31] * (i + 1)))
        rules[8] = rule_8
        rules[11] = rule_11

        messages = []
        line_num += 1
        for line in inp[line_num:]:
            messages.append(line)

        logger.debug(rules)
        logger.debug(messages)

        # precompute 42 and 31 possible values
        messages_42 = depth_first_search(rules, 42)
        messages_31 = depth_first_search(rules, 31)
        logger.debug(f"42: {messages_42}")
        logger.debug(f"31: {messages_31}")

        # messages from 42 and 31 are all 8 characters long
        # rule 8 will look like: [42], [42, 42], [42, 42, 42], ...
        # rule 11 will look like: [42, 31], [42, 42, 31, 31], [42, 42, 42, 31, 31, 31] ...
        # there will always be at least one rule 8 before the character limit
        # working through each possible combination of the complete rule 42 and 31
        # possible message list up to the maximum len of the longest message
        # and seeing if there are any matches with the rules

        # building valid messages from 0
        possible_combinations = []
        max_42 = 10
        for i in range(2, max_42):
            for j in range(1, i):
                possible_combinations.append((i, j))
        logger.debug(possible_combinations)

        valid_messages = 0
        chunk_length = len(messages_42[0])
        for message in messages:
            chunks = [
                message[i : i + chunk_length]
                for i in range(0, len(message), chunk_length)
            ]
            # breaking message in to 8 character chunks
            for combo in possible_combinations:
                try:
                    valid_message = True
                    k = 0
                    for i in range(combo[0]):
                        if chunks[k] not in messages_42:
                            valid_message = False
                        k += 1

                    for j in range(combo[1]):
                        if chunks[k] not in messages_31:
                            valid_message = False
                        k += 1

                    if k < len(chunks):
                        valid_message = False

                    if valid_message:
                        logger.debug(f"Valid Message: {message}")
                        valid_messages += 1
                        break
                except IndexError:
                    pass

        return valid_messages


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

    # test_input = [
    #     "0: 1 2",
    #     '1: "a"',
    #     "2: 1 3 | 3 1",
    #     '3: "b"',
    #     "",
    #     "ababbb",
    #     "bababa",
    #     "abbbab",
    #     "aaabbb",
    #     "aaaabbb",
    # ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=2,
    )
    part_1.submit_answer()

    test_input = [
        "42: 9 14 | 10 1",
        "9: 14 27 | 1 26",
        "10: 23 14 | 28 1",
        '1: "a"',
        "11: 42 31",
        "5: 1 14 | 15 1",
        "19: 14 1 | 14 14",
        "12: 24 14 | 19 1",
        "16: 15 1 | 14 14",
        "31: 14 17 | 1 13",
        "6: 14 14 | 1 14",
        "2: 1 24 | 14 4",
        "0: 8 11",
        "13: 14 3 | 1 12",
        "15: 1 | 14",
        "17: 14 2 | 1 7",
        "23: 25 1 | 22 14",
        "28: 16 1",
        "4: 1 1",
        "20: 14 14 | 1 15",
        "3: 5 14 | 16 1",
        "27: 1 6 | 14 18",
        '14: "b"',
        "21: 14 1 | 1 14",
        "25: 1 1 | 1 14",
        "22: 14 14",
        "8: 42",
        "26: 14 22 | 1 20",
        "18: 15 15",
        "7: 14 5 | 1 21",
        "24: 14 1",
        "",
        "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
        "bbabbbbaabaabba",
        "babbbbaabbbbbabbbbbbaabaaabaaa",
        "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
        "bbbbbbbaaaabbbbaaabbabaaa",
        "bbbababbbbaaaaaaaabbababaaababaabab",
        "ababaaaaaabaaab",
        "ababaaaaabbbaba",
        "baabbaaaabbaaaababbaababb",
        "abbbbabbbbaaaababbbbbbaaaababb",
        "aaaaabbaabaaaaababaa",
        "aaaabbaaaabbaaa",
        "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
        "babaaabbbaaabaababbaabababaaab",
        "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=12,
    )
    part_2.submit_answer()

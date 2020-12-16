#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        i = 0
        line = inp[i]
        rules = {}
        # handling initial rules
        while line != "":
            rule, allowable_values = line.split(": ")
            lower_values, upper_values = allowable_values.split(" or ")
            allowables = [int(val) for val in lower_values.split("-")] + [
                int(val) for val in upper_values.split("-")
            ]
            # logging.debug(f"New Rule: {rule} ({allowables[0]} to {allowables[1]} or {allowables[2]} to {allowables[3]})")
            rules[rule] = allowables
            i += 1
            line = inp[i]

        # handling my ticket
        i += 2
        # line = inp[i]
        # my_ticket = [int(val) for val in line.split(",")]
        # logger.debug(f"My Ticket: {my_ticket}")
        i += 3

        # handling nearby other tickets
        nearby_tickets = []
        for line in inp[i:]:
            new_ticket = [int(val) for val in line.split(",")]
            # logger.debug(f"Nearby Ticket: {new_ticket}")
            nearby_tickets.append(new_ticket)

        # brute force check every value against every rule
        errors = []
        for ticket in nearby_tickets:
            for value in ticket:
                error_check = validate_value(value, rules)
                if error_check is False:
                    errors.append(value)

        return sum(errors)


def validate_value(value, rules):
    passes = False
    for rule_name, allowables in rules.items():
        if (value >= allowables[0] and value <= allowables[1]) or (
            value >= allowables[2] and value <= allowables[3]
        ):
            passes = True

    if passes:
        return True
    else:
        logger.debug(f"Found Error: {value}")
        return False


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        i = 0
        line = inp[i]
        rules = {}
        # handling initial rules
        while line != "":
            rule, allowable_values = line.split(": ")
            lower_values, upper_values = allowable_values.split(" or ")
            allowables = [int(val) for val in lower_values.split("-")] + [
                int(val) for val in upper_values.split("-")
            ]
            logging.debug(
                f"New Rule: {rule} ({allowables[0]} to {allowables[1]} or {allowables[2]} to {allowables[3]})"
            )
            rules[rule] = allowables
            i += 1
            line = inp[i]

        # handling my ticket
        i += 2
        line = inp[i]
        my_ticket = [int(val) for val in line.split(",")]
        logger.debug(f"My Ticket: {my_ticket}")
        i += 3

        # handling nearby other tickets
        nearby_tickets = []
        for line in inp[i:]:
            new_ticket = [int(val) for val in line.split(",")]
            logger.debug(f"Nearby Ticket: {new_ticket}")
            nearby_tickets.append(new_ticket)

        # brute force check every value against every rule, storing bad indexes
        invalid_ticket_indexes = []
        for index, ticket in enumerate(nearby_tickets):
            for value in ticket:
                error_check = validate_value(value, rules)
                if error_check is False:
                    invalid_ticket_indexes.append(index)

        # separate loop to delete tickets from list
        for index in invalid_ticket_indexes[::-1]:
            del nearby_tickets[index]

        logger.debug(f"Valid Tickets: {nearby_tickets}")

        # storing tickets as lists of fields once for later use
        # each list is a single index's values from all tickets
        # the list is stored in a list. The list index corresponds to the field index
        fields = [
            [ticket[field_index] for ticket in nearby_tickets]
            for field_index in range(len(my_ticket))
        ]

        # brute force check every ticket against every rule
        rule_to_field_map = {rule: [] for rule in rules}

        for rule, allowables in rules.items():
            for field_index, field_values in enumerate(fields):
                field_match = validate_field(field_values, allowables)
                if field_match:
                    rule_to_field_map[rule].append(field_index)

        # Now iterate through the mapping, adding any indexes from lists of length one
        # to the final mapping dictionary and then removing that index from all other
        # lists.
        # Continue to iterate through until the length of the final mapping is equal
        # to the length of the rule to field map
        final_mapping = {}
        while len(final_mapping) != len(rule_to_field_map):
            # find all field mappings with only one value
            single_indexes = []
            for rule, field_indexes in rule_to_field_map.items():
                if len(field_indexes) == 1:
                    index_value = field_indexes[0]
                    single_indexes.append(index_value)
                    final_mapping[rule] = index_value
                    logger.debug(f"Final Mapping Found: {rule} to index {index_value}")
            # delete from all lists
            for value_to_remove in single_indexes:
                for rule in rule_to_field_map:
                    try:
                        rule_to_field_map[rule].remove(value_to_remove)
                    except ValueError:
                        pass
            logger.debug(f"New mapping: {rule_to_field_map}")

        departure_total = 1
        for rule, index in final_mapping.items():
            if rule[:9] == "departure":
                departure_total = departure_total * my_ticket[index]
        return departure_total


def validate_field(field_values, allowables):
    for value in field_values:
        if (value >= allowables[0] and value <= allowables[1]) or (
            value >= allowables[2] and value <= allowables[3]
        ):
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    day_number = 16
    test_input = [
        "class: 1-3 or 5-7",
        "row: 6-11 or 33-44",
        "seat: 13-40 or 45-50",
        "",
        "your ticket:",
        "7,1,14",
        "",
        "nearby tickets:",
        "7,3,47",
        "40,4,50",
        "55,2,20",
        "38,6,12",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=71,
    )
    part_1.submit_answer()

    test_input = [
        "departure 1: 0-1 or 4-19",
        "departure 2: 0-5 or 8-19",
        "not departure: 0-13 or 16-19",
        "",
        "your ticket:",
        "11,12,13",
        "",
        "nearby tickets:",
        "3,9,18",
        "15,1,5",
        "5,14,9",
        "10,49,8",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=132,
    )
    part_2.submit_answer()

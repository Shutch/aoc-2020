#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        memory = {}
        mask = "X" * 36
        for line in inp:
            command, value = line.split(" = ")
            if command == "mask":
                mask = value
                # logger.debug(f"New Mask: {value} 1: {one_mask:b} 0: {zero_mask:b}")
            elif "mem" in command:
                location = int(command[4:-1])  # number inside square brackets
                value = int(value)
                for address, new_value in enumerate(mask):
                    if new_value == "1":
                        value = value | (1 << (len(mask) - address - 1))
                    elif new_value == "0":
                        value = value & ~(1 << (len(mask) - address - 1))
                memory[location] = value

            else:
                raise ValueError(f"Command not recognized: {command} = {value}")
        # logger.debug(f"Final Memory: {memory}")
        return sum(memory.values())


def get_addresses(address_list, affected_addresses):
    # logger.debug(f"Scanning Address: {''.join(address_list)}")
    complete_address = True
    new_address = address_list.copy()
    for bit_address, bit_value in enumerate(address_list):
        if bit_value == "X":
            complete_address = False
            new_address[bit_address] = "1"
            get_addresses(new_address, affected_addresses)
            new_address[bit_address] = "0"
            get_addresses(new_address, affected_addresses)
    if complete_address:
        int_address = int("".join(new_address), 2)
        affected_addresses.append(int_address)
    return affected_addresses


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        memory = {}
        mask = "0" * 36
        for line in inp:
            command, value = line.split(" = ")
            if command == "mask":
                mask = value
                ones = [i for i, j in enumerate(mask) if j == "1"]
                xs = [i for i, j in enumerate(mask) if j == "X"]
                # logger.debug(f"New Mask: {value}")
            elif "mem" in command:
                address = int(command[4:-1])  # number inside square brackets
                address_list = list(format(address, "036b"))
                # first pass to overwrite mask locations with value of 1 and X
                for bit in ones:
                    address_list[bit] = "1"
                for bit in xs:
                    address_list[bit] = "X"

                affected_addresses = get_addresses(address_list, [])
                # writing to all addresses
                for a in affected_addresses:
                    value = int(value)
                    # logger.debug(f"Writing {value} to {a}")
                    memory[a] = value

            else:
                raise ValueError(f"Command not recognized: {command} = {value}")
        # logger.debug(f"Final Memory: {memory}")
        return sum(memory.values())


if __name__ == "__main__":
    day_number = 14
    test_input = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=165,
    )
    part_1.submit_answer()

    test_input = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=208,
    )
    part_2.submit_answer()

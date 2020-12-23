#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging
from collections import deque

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        cups = MappedDoublyLinkedCircularList()
        for value in inp[0]:
            cups.append_node_at_tail(Node(int(value)))
        min_cup = cups.min()
        max_cup = cups.max()
        len_cup = len(cups.map)
        # logger.debug(cups)
        # logger.debug(f"Min: {min_cup}, Max: {max_cup}, Total: {len_cup}")
        moves = 100
        current_cup = cups.head
        for turn in range(0, moves):
            # logger.debug(f"-- Turn {turn + 1} --")
            # logger.debug(f"Cups {cups}, Current {current_cup.value}")

            # removing 3 cups after current cup
            cup_1 = current_cup.next
            cup_2 = cup_1.next
            cup_3 = cup_2.next
            current_cup.next = cup_3.next
            # logger.debug(f"Picked up {cup_1.value} {cup_2.value} {cup_3.value}")

            # finding current cups value - 1
            target_value = (
                current_cup.value - 1 if current_cup.value > min_cup else max_cup
            )
            selected_cup = None
            while selected_cup is None:
                if target_value in [cup_1.value, cup_2.value, cup_3.value]:
                    target_value = (
                        target_value - 1 if target_value > min_cup else max_cup
                    )
                else:
                    selected_cup = cups[target_value]
                    # logger.debug(f"Selected cup {selected_cup.value}")

            # setting previously picked up cups after the new selected cup
            cup_3.next = selected_cup.next
            selected_cup.next = cup_1

            # logger.debug(f"{selected_cup} {cup_1} {cup_2} {cup_3} {cup_4}")

            # setting up for the next round
            current_cup = current_cup.next

        head_cup = current_cup
        for i in range(len_cup - (turn % len_cup) - 1):
            head_cup = head_cup.next
        cups.head = head_cup

        answer = ""
        current_cup = cups[1].next
        for i in range(len_cup - 1):
            answer = answer + str(current_cup.value)
            current_cup = current_cup.next
        return answer


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        total_cups = 1_000_000
        cups = MappedDoublyLinkedCircularList()
        for value in inp[0]:
            cups.append_node_at_tail(Node(int(value)))
        for value in range(cups.max() + 1, total_cups + 1):
            cups.append_node_at_tail(Node(value))
        min_cup = cups.min()
        max_cup = cups.max()
        len_cup = len(cups.map)
        # logger.debug(f"Min: {min_cup}, Max: {max_cup}, Total: {len_cup}")
        moves = 10_000_000
        current_cup = cups.head
        for turn in range(0, moves):
            # logger.debug(f"-- Turn {turn + 1} --")
            # logger.debug(f"Cups {cups}, Current {current_cup.value}")

            # removing 3 cups after current cup
            cup_1 = current_cup.next
            cup_2 = cup_1.next
            cup_3 = cup_2.next
            current_cup.next = cup_3.next
            # logger.debug(f"Picked up {cup_1.value} {cup_2.value} {cup_3.value}")

            # finding current cups value - 1
            target_value = (
                current_cup.value - 1 if current_cup.value > min_cup else max_cup
            )
            selected_cup = None
            while selected_cup is None:
                if target_value in [cup_1.value, cup_2.value, cup_3.value]:
                    target_value = (
                        target_value - 1 if target_value > min_cup else max_cup
                    )
                else:
                    selected_cup = cups[target_value]
                    # logger.debug(f"Selected cup {selected_cup.value}")

            # setting previously picked up cups after the new selected cup
            cup_3.next = selected_cup.next
            selected_cup.next = cup_1

            # logger.debug(f"{selected_cup} {cup_1} {cup_2} {cup_3} {cup_4}")

            # setting up for the next round
            current_cup = current_cup.next
        head_cup = current_cup
        for i in range(len_cup - (turn % len_cup) - 1):
            head_cup = head_cup.next
        cups.head = head_cup

        return cups[1].next.value * cups[1].next.next.value


class Node:
    def __init__(self, value, p=None, n=None):
        self.value = value
        self.next = n

    def __repr__(self):
        return f"{self.value} (-> {self.next.value})"


class MappedDoublyLinkedCircularList:
    def __init__(self):
        self.map = {}
        self.head = None
        self.tail = None

    def __getitem__(self, item):
        node = self.map[item]
        return node

    def append_node_at_tail(self, node):
        if self.head is None:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        node.next = self.head
        self.map[node.value] = node

    def min(self):
        return min(self.map.keys())

    def max(self):
        return max(self.map.keys())

    def __str__(self):
        node_order = "["
        node = self.head
        node_order = f"[{self.head.value}, "
        node = node.next
        while node != self.head:
            node_order = node_order + str(node.value) + ", "
            node = node.next
        return node_order[:-2] + "]"


if __name__ == "__main__":
    day_number = 23
    test_input = ["389125467"]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer="67384529",
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=149245887792,
    )
    part_2.submit_answer()

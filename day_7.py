#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Graph:
    def __init__(self):
        self.bags = {}
        self.count = 0

    def find_bag(self, bag_color):
        return self.bags.get(bag_color, None)
        # raise ValueError(f"Bag {bag_color} not found")

    def add_bag(self, bag_node):
        self.bags[bag_node.color] = bag_node

    def find_occurences(self, bag_color):
        occurences = 0
        for bag in self.bags.values():
            if self.contains_bag(bag.color, bag_color):
                occurences += 1
        return occurences

    def contains_bag(self, current_bag_color, search_bag_color):
        # check children
        bag = self.find_bag(current_bag_color)
        for child_color, number in bag.children.items():
            contains_bag = self.contains_bag(child_color, search_bag_color)
            if contains_bag or child_color == search_bag_color:
                return True
        return False

    def find_count(self, bag_color, total_count=0, multiplier=1):
        main_bag = self.find_bag(bag_color)
        for child_bag_color, child_bag_count in main_bag.children.items():
            total_count += child_bag_count * multiplier
            total_count = self.find_count(
                child_bag_color, total_count, multiplier * child_bag_count
            )
        return total_count

    def __str__(self):
        return f"{self.bags}"


class BagNode:
    def __init__(self, color, children):
        self.color = color
        self.children = children  # dict{color: number}

    def __repr__(self):
        return f"{self.color}{self.children}"

    def __str__(self):
        return f"{self.color}: {self.children}"


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        graph = Graph()
        full_inp = "".join(inp)
        inp = full_inp.split(".")[:-1]  # blank string at the end
        for bag_type in inp:
            bag_type = bag_type.replace(" bags", "")
            bag_type = bag_type.replace(" bag", "")
            subject_bag, contained_bags = bag_type.split(" contain ")
            if contained_bags == "no other":
                contained_bags = {}
            else:
                contained_bags = contained_bags.split(", ")
                contained_bags = {
                    bag.split(" ", 1)[1]: int(bag.split(" ", 1)[0])
                    for bag in contained_bags
                }
            bag = BagNode(subject_bag, contained_bags)
            graph.add_bag(bag)
        occurences = graph.find_occurences("shiny gold")
        return occurences


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        graph = Graph()
        full_inp = "".join(inp)
        inp = full_inp.split(".")[:-1]  # blank string at the end
        for bag_type in inp:
            bag_type = bag_type.replace(" bags", "")
            bag_type = bag_type.replace(" bag", "")
            subject_bag, contained_bags = bag_type.split(" contain ")
            if contained_bags == "no other":
                contained_bags = {}
            else:
                contained_bags = contained_bags.split(", ")
                contained_bags = {
                    bag.split(" ", 1)[1]: int(bag.split(" ", 1)[0])
                    for bag in contained_bags
                }
            bag = BagNode(subject_bag, contained_bags)
            graph.add_bag(bag)
        total_count = graph.find_count("shiny gold")
        return total_count


if __name__ == "__main__":
    day_number = 7
    test_input = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=4,
    )
    part_1.submit_answer()

    test_input = [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=126,
    )
    part_2.submit_answer()

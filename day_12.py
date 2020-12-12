#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Ship1:
    def __init__(self):
        self.x = 0  # x+ is east
        self.y = 0  # y+ is north
        self.heading = 90  # north is 0, CW is positive

    def step(self, action, amount):
        if action == "N":
            self.y += amount
        elif action == "S":
            self.y -= amount
        elif action == "E":
            self.x += amount
        elif action == "W":
            self.x -= amount
        elif action == "L":
            new_heading = self.heading - amount
            self.heading = new_heading % 360
        elif action == "R":
            new_heading = self.heading + amount
            self.heading = new_heading % 360
        elif action == "F":
            if self.heading == 0:
                self.y += amount
            elif self.heading == 90:
                self.x += amount
            elif self.heading == 180:
                self.y -= amount
            elif self.heading == 270:
                self.x -= amount
            else:
                raise ValueError(f"Heading value not recognized: {self.heading}")
        else:
            raise ValueError(f"Action value not recognized: {action}")

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        ship = Ship1()
        for step in inp:
            action = step[0]
            amount = int(step[1:])
            ship.step(action, amount)
        return ship.manhattan_distance()


class Ship2:
    def __init__(self):
        self.x = 0  # x+ is east
        self.y = 0  # y+ is north
        self.waypoint_x = 10  # relative to the ship
        self.waypoint_y = 1  # relative to the ship

    def step(self, action, amount):
        if action == "N":
            self.waypoint_y += amount
        elif action == "S":
            self.waypoint_y -= amount
        elif action == "E":
            self.waypoint_x += amount
        elif action == "W":
            self.waypoint_x -= amount
        elif action == "L":
            if amount == 90:
                old_x = self.waypoint_x
                old_y = self.waypoint_y
                self.waypoint_x = -old_y
                self.waypoint_y = old_x
            elif amount == 180:
                self.waypoint_x = -self.waypoint_x
                self.waypoint_y = -self.waypoint_y
            elif amount == 270:
                old_x = self.waypoint_x
                old_y = self.waypoint_y
                self.waypoint_x = old_y
                self.waypoint_y = -old_x
            else:
                raise ValueError(f"Heading value not recognized: {action}{amount}")
        elif action == "R":
            if amount == 90:
                old_x = self.waypoint_x
                old_y = self.waypoint_y
                self.waypoint_x = old_y
                self.waypoint_y = -old_x
            elif amount == 180:
                self.waypoint_x = -self.waypoint_x
                self.waypoint_y = -self.waypoint_y
            elif amount == 270:
                old_x = self.waypoint_x
                old_y = self.waypoint_y
                self.waypoint_x = -old_y
                self.waypoint_y = old_x
            else:
                raise ValueError(f"Heading value not recognized: {action}{amount}")
        elif action == "F":
            self.x += self.waypoint_x * amount
            self.y += self.waypoint_y * amount
        else:
            raise ValueError(f"Action value not recognized: {action}")

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        ship = Ship2()
        for step in inp:
            action = step[0]
            amount = int(step[1:])
            ship.step(action, amount)
        return ship.manhattan_distance()


if __name__ == "__main__":
    day_number = 12
    test_input = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=25,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=286,
    )
    part_2.submit_answer()

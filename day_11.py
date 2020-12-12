#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class WaitingArea:
    def __init__(self, seats, width, height):
        self.seats = seats
        self.previous_seats = {}
        self.width = width
        self.height = height

    def find_seat(self, x, y):
        return self.previous_seats.get((x, y), 0)

    def count_seats(self):
        return sum(self.seats.values())

    def update_seats_1(self):
        self.previous_seats = self.seats.copy()
        for coords, status in self.previous_seats.items():
            adjacent_seats = self.find_adjacent_seats_1(coords[0], coords[1])
            if sum(adjacent_seats.values()) == 0 and status == 0:
                self.seats[coords] = 1
            elif sum(adjacent_seats.values()) >= 4 and status == 1:
                self.seats[coords] = 0

    def find_adjacent_seats_1(self, x, y):
        adjacent_seats = {}
        for x_adj in [-1, 0, 1]:
            for y_adj in [-1, 0, 1]:
                if not (x_adj == 0 and y_adj == 0):
                    seat_status = self.find_seat(x + x_adj, y + y_adj)
                    adjacent_seats[(x + x_adj, y + y_adj)] = seat_status
        return adjacent_seats

    def update_seats_2(self):
        self.previous_seats = self.seats.copy()
        for coords, status in self.previous_seats.items():
            adjacent_seats = self.find_adjacent_seats_2(coords[0], coords[1])
            if sum(adjacent_seats) == 0 and status == 0:
                self.seats[coords] = 1
            elif sum(adjacent_seats) >= 5 and status == 1:
                self.seats[coords] = 0

    def find_adjacent_seats_2(self, x, y):
        adjacent_seats = []
        directions = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

        for direction in directions:
            seat = self.find_directional_seat(x, y, direction[0], direction[1])
            adjacent_seats.append(seat)
        return adjacent_seats

    def find_directional_seat(self, x, y, x_adj, y_adj):
        seat = 0
        new_x = x + x_adj
        new_y = y + y_adj
        while new_x >= 0 and new_y >= 0 and new_x < self.width and new_y < self.height:
            seat = self.previous_seats.get((new_x, new_y), None)
            if seat is not None:
                return seat
            new_x = new_x + x_adj
            new_y = new_y + y_adj
        return 0

    def __str__(self):
        return_str = "\n"
        for y in range(0, self.height):
            for x in range(0, self.width):
                seat = self.seats.get((x, y), -1)
                if seat == 0:
                    return_str = return_str + "L"
                elif seat == 1:
                    return_str = return_str + "#"
                else:
                    return_str = return_str + "."
            return_str = return_str + "\n"
        return return_str


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        # seat X and Y values are from top left, X+ to the right, Y+ down
        height = len(inp)
        width = len(inp[0])
        seats = {}
        for y, row in enumerate(inp):
            for x, col in enumerate(row):
                if col == "L":
                    seats[(x, y)] = 0
        waiting_area = WaitingArea(seats, width, height)
        while waiting_area.seats != waiting_area.previous_seats:
            waiting_area.update_seats_1()
        return waiting_area.count_seats()


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        # seat X and Y values are from top left, X+ to the right, Y+ down
        height = len(inp)
        width = len(inp[0])
        seats = {}
        for y, row in enumerate(inp):
            for x, col in enumerate(row):
                if col == "L":
                    seats[(x, y)] = 0
        waiting_area = WaitingArea(seats, width, height)
        while waiting_area.seats != waiting_area.previous_seats:
            waiting_area.update_seats_2()
        return waiting_area.count_seats()


if __name__ == "__main__":
    day_number = 11
    test_input = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=37,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=26,
    )
    part_2.submit_answer()

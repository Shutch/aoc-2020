#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        # precomputing neighbor arrays
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    neighbors.append((x, y, z))

        del neighbors[13]  # origin point

        grid = {}
        z = 0
        for y, line in enumerate(inp):
            for x, char in enumerate(line):
                if char == "#":
                    grid[(x, y, z)] = 1
                    for x_n, y_n, z_n in neighbors:
                        neighbor_coords = (x + x_n, y + y_n, z + z_n)
                        existing_value = grid.get(neighbor_coords, 0)
                        grid[neighbor_coords] = existing_value

        for cycle in range(6):
            # logger.debug(f"Cycle: {cycle}{stringify_3D_grid(grid)}")
            next_grid = grid.copy()
            for (x, y, z), value in grid.items():
                active_neighbors = sum(
                    [
                        grid.get((x + x_n, y + y_n, z + z_n), 0)
                        for x_n, y_n, z_n in neighbors
                    ]
                )
                if value == 1:
                    if active_neighbors == 2 or active_neighbors == 3:
                        next_grid[(x, y, z)] = 1
                    else:
                        next_grid[(x, y, z)] = 0
                if value == 0 and active_neighbors == 3:
                    next_grid[(x, y, z)] = 1
                    # adding new neighbors
                    for x_n, y_n, z_n in neighbors:
                        neighbor_coords = (x + x_n, y + y_n, z + z_n)
                        existing_value = next_grid.get(neighbor_coords, 0)
                        next_grid[neighbor_coords] = existing_value
            grid = next_grid
        active_cells = sum(grid.values())
        return active_cells


def stringify_3D_grid(grid):
    x_min = min([coords[0] for coords in grid.keys()])
    x_max = max([coords[0] for coords in grid.keys()])
    y_min = min([coords[1] for coords in grid.keys()])
    y_max = max([coords[1] for coords in grid.keys()])
    z_min = min([coords[2] for coords in grid.keys()])
    z_max = max([coords[2] for coords in grid.keys()])
    print_string = "\n"
    for z in range(z_min, z_max + 1):
        print_string = print_string + f"Z level {z}\n"
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                cell_value = grid.get((x, y, z), 0)
                if cell_value == 0:
                    print_string = print_string + "."
                else:
                    print_string = print_string + "#"
            print_string = print_string + "\n"
        print_string = print_string + "\n"
    return print_string


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        # precomputing neighbor arrays
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        neighbors.append((x, y, z, w))

        del neighbors[neighbors.index((0, 0, 0, 0))]  # origin point

        grid = {}
        z = 0
        w = 0
        for y, line in enumerate(inp):
            for x, char in enumerate(line):
                if char == "#":
                    grid[(x, y, z, w)] = 1
                    for x_n, y_n, z_n, w_n in neighbors:
                        neighbor_coords = (x + x_n, y + y_n, z + z_n, w + w_n)
                        existing_value = grid.get(neighbor_coords, 0)
                        grid[neighbor_coords] = existing_value

        for cycle in range(6):
            logger.debug(f"Cycle: {cycle}{stringify_4D_grid(grid)}")
            next_grid = grid.copy()
            for (x, y, z, w), value in grid.items():
                active_neighbors = sum(
                    [
                        grid.get((x + x_n, y + y_n, z + z_n, w + w_n), 0)
                        for x_n, y_n, z_n, w_n in neighbors
                    ]
                )
                if value == 1:
                    if active_neighbors == 2 or active_neighbors == 3:
                        next_grid[(x, y, z, w)] = 1
                    else:
                        next_grid[(x, y, z, w)] = 0
                if value == 0 and active_neighbors == 3:
                    next_grid[(x, y, z, w)] = 1
                    # adding new neighbors
                    for x_n, y_n, z_n, w_n in neighbors:
                        neighbor_coords = (x + x_n, y + y_n, z + z_n, w + w_n)
                        existing_value = next_grid.get(neighbor_coords, 0)
                        next_grid[neighbor_coords] = existing_value
            grid = next_grid
        active_cells = sum(grid.values())
        return active_cells


def stringify_4D_grid(grid):
    x_min = min([coords[0] for coords in grid.keys()])
    x_max = max([coords[0] for coords in grid.keys()])
    y_min = min([coords[1] for coords in grid.keys()])
    y_max = max([coords[1] for coords in grid.keys()])
    z_min = min([coords[2] for coords in grid.keys()])
    z_max = max([coords[2] for coords in grid.keys()])
    w_min = min([coords[3] for coords in grid.keys()])
    w_max = max([coords[3] for coords in grid.keys()])
    print_string = "\n"
    for w in range(w_min, w_max + 1):
        for z in range(z_min, z_max + 1):
            print_string = print_string + f"Z level {z}, W level {w}\n"
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    cell_value = grid.get((x, y, z, w), 0)
                    if cell_value == 0:
                        print_string = print_string + "."
                    else:
                        print_string = print_string + "#"
                print_string = print_string + "\n"
            print_string = print_string + "\n"
        return print_string


if __name__ == "__main__":
    day_number = 17
    test_input = [
        ".#.",
        "..#",
        "###",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=112,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=848,
    )
    part_2.submit_answer()

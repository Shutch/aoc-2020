#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging
import pprint

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        # parsing
        tiles = {}
        for line in inp:
            if "Tile" in line:
                current_tile_id = int(line[5:-1])
                tiles[current_tile_id] = {}
                y = 0
            else:
                for x, char in enumerate(line):
                    if char == "#":
                        tiles[current_tile_id][(x, y)] = 1
                    elif char == ".":
                        tiles[current_tile_id][(x, y)] = 0
                    else:
                        raise ValueError(f"Unexpected character {char}")
                y += 1

        # building edge list for each tile, moving in a clockwise direction
        # this includes reverse directions
        tile_edges = {}
        for tile_id, tile in tiles.items():
            edges = []
            edge = []

            # top edge
            for x in range(10):
                edge.append(tiles[tile_id][(x, 0)])
            edges.append(edge)
            edges.append(list(reversed(edge)))

            edge = []
            # bottom edge
            for x in range(9, -1, -1):
                edge.append(tiles[tile_id][(x, 9)])
            edges.append(edge)
            edges.append(list(reversed(edge)))

            edge = []
            # right edge
            for y in range(10):
                edge.append(tiles[tile_id][(9, y)])
            edges.append(edge)
            edges.append(list(reversed(edge)))

            edge = []
            # left edge
            for y in range(9, -1, -1):
                edge.append(tiles[tile_id][(0, y)])
            edges.append(edge)
            edges.append(list(reversed(edge)))

            tile_edges[tile_id] = edges

        # finding matched sides
        tile_matches = {}
        for tile_id, edges in tile_edges.items():
            matching_edges = 0
            for edge in edges:
                for match_tile_id, match_edges in tile_edges.items():
                    if edge in match_edges:
                        matching_edges += 1
            # logger.debug(f"Tile {tile_id} - Matching edges: {matching_edges}")
            tile_matches[tile_id] = matching_edges

        min_match_tile_ids = [
            tile_id
            for tile_id, match_number in tile_matches.items()
            if match_number == min(tile_matches.values())
        ]
        id_mult = 1
        # logger.debug(
        #     f"{len(min_match_tile_ids)} with match number of {min(tile_matches.values())}"
        # )
        for match_number in min_match_tile_ids:
            id_mult = id_mult * match_number
        return id_mult


def print_tile(tile_id, tile):
    print_str = f"Tile: {tile_id}\n"
    x_coords = [key[0] for key, value in tile.items()]
    y_coords = [key[1] for key, value in tile.items()]
    for y in range(min(y_coords), max(y_coords) + 1):
        for x in range(min(x_coords), max(x_coords) + 1):
            value = tile[(x, y)]
            if value == 1:
                print_str = print_str + "#"
            elif value == 0:
                print_str = print_str + "."
            else:
                raise ValueError(f"Unexpected value {value}")
        print_str = print_str + "\n"
    return print_str


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        # parsing
        tiles = {}
        for line in inp:
            if "Tile" in line:
                current_tile_id = int(line[5:-1])
                tiles[current_tile_id] = {}
                y = 0
            else:
                for x, char in enumerate(line):
                    if char == "#":
                        tiles[current_tile_id][(x, y)] = 1
                    elif char == ".":
                        tiles[current_tile_id][(x, y)] = 0
                    else:
                        raise ValueError(f"Unexpected character {char}")
                y += 1

        # building edge list for each tile, moving in a clockwise direction
        # this includes reverse directions
        tile_edges = {}
        for tile_id, tile in tiles.items():
            edges = []

            # first letter is cardinal direction of edge (N, E, S, W)
            # second letter is normal or reverse (N, R)
            # top edge
            edge = []
            for x in range(10):
                edge.append(tiles[tile_id][(x, 0)])
            edges.append({"edge": edge, "orientation": 0, "flipped": False})
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append({"edge": flipped_edge, "orientation": 0, "flipped": True})

            # bottom edge
            edge = []
            for x in range(9, -1, -1):
                edge.append(tiles[tile_id][(x, 9)])
            edges.append({"edge": edge, "orientation": 180, "flipped": False})
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append({"edge": flipped_edge, "orientation": 180, "flipped": True})

            # right edge
            edge = []
            for y in range(10):
                edge.append(tiles[tile_id][(9, y)])
            edges.append({"edge": edge, "orientation": 90, "flipped": False})
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append({"edge": flipped_edge, "orientation": 270, "flipped": True})

            # left edge
            edge = []
            for y in range(9, -1, -1):
                edge.append(tiles[tile_id][(0, y)])
            edges.append({"edge": edge, "orientation": 270, "flipped": False})
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append({"edge": flipped_edge, "orientation": 90, "flipped": True})

            tile_edges[tile_id] = edges

        # Starting with the lowest ID tile and building orientation and location map
        tile_locations = {}
        starting_tile_id = min(tiles)
        unset_tile_ids = list(tile_edges.keys())
        unset_tile_ids.remove(starting_tile_id)
        set_tile_ids = [starting_tile_id]
        current_tile = {
            "coords": (0, 0),
            "orientation": 0,  # 0 is N, 90 is E, 180 is S
            "flipped": False,
        }
        tile_locations[starting_tile_id] = current_tile
        while len(unset_tile_ids) > 0:
            for index in range(len(set_tile_ids) - 1, -1, -1):
                current_tile_id = set_tile_ids[index]
                current_tile = tile_locations[current_tile_id]
                # logging.debug(f"Now matching {current_tile_id}")
                for edge in tile_edges[current_tile_id]:
                    if edge["flipped"] == current_tile["flipped"]:
                        for matching_tile_id in unset_tile_ids:
                            for matching_edge in tile_edges[matching_tile_id]:
                                if edge["edge"] == matching_edge["edge"]:
                                    # logger.debug(
                                    #     f"\nmatch {current_tile_id} ({edge})\n with {matching_tile_id} ({matching_edge})"
                                    # )

                                    orientation = (
                                        edge["orientation"]
                                        + matching_edge["orientation"]
                                        + current_tile["orientation"]
                                        + 180
                                    ) % 360

                                    if (
                                        edge["orientation"]
                                        + current_tile["orientation"]
                                    ) % 360 == 0:
                                        coords = (
                                            current_tile["coords"][0],
                                            current_tile["coords"][1] - 1,
                                        )
                                    elif (
                                        edge["orientation"]
                                        + current_tile["orientation"]
                                    ) % 360 == 90:
                                        coords = (
                                            current_tile["coords"][0] + 1,
                                            current_tile["coords"][1],
                                        )
                                    elif (
                                        edge["orientation"]
                                        + current_tile["orientation"]
                                    ) % 360 == 180:
                                        coords = (
                                            current_tile["coords"][0],
                                            current_tile["coords"][1] + 1,
                                        )
                                    elif (
                                        edge["orientation"]
                                        + current_tile["orientation"]
                                    ) % 360 == 270:
                                        coords = (
                                            current_tile["coords"][0] - 1,
                                            current_tile["coords"][1],
                                        )
                                    else:
                                        raise ValueError(current_tile["orientation"])

                                    flipped = not matching_edge["flipped"]
                                    tile_locations[matching_tile_id] = {
                                        "coords": coords,
                                        "orientation": orientation,
                                        "flipped": flipped,
                                    }
                                    set_tile_ids.append(matching_tile_id)
                                    unset_tile_ids.remove(matching_tile_id)
                del set_tile_ids[index]

        # Removing edges and building grid
        full_grid = {}
        mult = 8
        for tile_id, tile_info in tile_locations.items():
            tile = tiles[tile_id]
            if tile_info["flipped"]:
                tile = flip_tile_horizontal(tile)
            tile = rotate_tile_CW(tile, rotations=tile_info["orientation"] // 90)
            x_coords = [key[0] for key, value in tile.items()]
            y_coords = [key[1] for key, value in tile.items()]
            for y in range(min(y_coords) + 1, max(y_coords)):
                for x in range(min(x_coords) + 1, max(x_coords)):
                    x_val = x + tile_locations[tile_id]["coords"][0] * mult
                    y_val = y + tile_locations[tile_id]["coords"][1] * mult
                    full_grid[(x_val, y_val)] = tile[(x, y)]

        # normalizing grid to (0, 0) top left corner so rotations actually work
        x_shift = min([key[0] for key, value in full_grid.items()])
        y_shift = min([key[1] for key, value in full_grid.items()])
        full_grid = {
            (x - x_shift, y - y_shift): value for (x, y), value in full_grid.items()
        }

        # converting sea monster to dictionary coords
        # only need the # symbols
        sea_monster_str = [
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   ",
        ]
        sea_monster = {}
        for y, line in enumerate(sea_monster_str):
            for x, char in enumerate(line):
                if char == "#":
                    sea_monster[(x, y)] = 1

        # checking each orientation for sea monsters
        x_size = max([key[0] for key, value in full_grid.items()])
        y_size = max([key[1] for key, value in full_grid.items()])
        total_sea_monsters = 0
        for i in range(2):
            for j in range(4):
                for y in range(y_size + 1):
                    for x in range(x_size + 1):
                        monster = True
                        for monster_x, monster_y in sea_monster.keys():
                            value = full_grid.get((x + monster_x, y + monster_y), 0)
                            if value == 0:
                                monster = False
                        if monster:
                            total_sea_monsters += 1
                            logger.debug(
                                f"Found a sea monster in {i}, {j}. Total {total_sea_monsters}"
                            )

                # rotating for next round
                full_grid = rotate_tile_CW(full_grid)
            # flipping for next round
            full_grid = flip_tile_horizontal(full_grid)

        waves = sum(full_grid.values()) - total_sea_monsters * sum(sea_monster.values())
        return waves


def rotate_tile_CW(tile, rotations=1):
    rot_tile = tile.copy()
    temp_tile = tile.copy()
    for i in range(rotations):
        x_coords = [key[0] for key, value in temp_tile.items()]
        y_coords = [key[1] for key, value in temp_tile.items()]
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                rot_tile[(max_y - y, x)] = temp_tile[(x, y)]
        temp_tile = rot_tile.copy()
    return rot_tile


def flip_tile_horizontal(tile):
    rot_tile = {}
    x_coords = [key[0] for key, value in tile.items()]
    y_coords = [key[1] for key, value in tile.items()]
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            rot_tile[(max_x - x, y)] = tile[(x, y)]
    return rot_tile


if __name__ == "__main__":
    day_number = 20
    test_input = [
        "Tile 2311:",
        "..##.#..#.",
        "##..#.....",
        "#...##..#.",
        "####.#...#",
        "##.##.###.",
        "##...#.###",
        ".#.#.#..##",
        "..#....#..",
        "###...#.#.",
        "..###..###",
        "",
        "Tile 1951:",
        "#.##...##.",
        "#.####...#",
        ".....#..##",
        "#...######",
        ".##.#....#",
        ".###.#####",
        "###.##.##.",
        ".###....#.",
        "..#.#..#.#",
        "#...##.#..",
        "",
        "Tile 1171:",
        "####...##.",
        "#..##.#..#",
        "##.#..#.#.",
        ".###.####.",
        "..###.####",
        ".##....##.",
        ".#...####.",
        "#.##.####.",
        "####..#...",
        ".....##...",
        "",
        "Tile 1427:",
        "###.##.#..",
        ".#..#.##..",
        ".#.##.#..#",
        "#.#.#.##.#",
        "....#...##",
        "...##..##.",
        "...#.#####",
        ".#.####.#.",
        "..#..###.#",
        "..##.#..#.",
        "",
        "Tile 1489:",
        "##.#.#....",
        "..##...#..",
        ".##..##...",
        "..#...#...",
        "#####...#.",
        "#..#.#.#.#",
        "...#.#.#..",
        "##.#...##.",
        "..##.##.##",
        "###.##.#..",
        "",
        "Tile 2473:",
        "#....####.",
        "#..#.##...",
        "#.##..#...",
        "######.#.#",
        ".#...#.#.#",
        ".#########",
        ".###.#..#.",
        "########.#",
        "##...##.#.",
        "..###.#.#.",
        "",
        "Tile 2971:",
        "..#.#....#",
        "#...###...",
        "#.#.###...",
        "##.##..#..",
        ".#####..##",
        ".#..####.#",
        "#..#.#..#.",
        "..####.###",
        "..#.#.###.",
        "...#.#.#.#",
        "",
        "Tile 2729:",
        "...#.#.#.#",
        "####.#....",
        "..#.#.....",
        "....#..#.#",
        ".##..##.#.",
        ".#.####...",
        "####.#.#..",
        "##.####...",
        "##..#.##..",
        "#.##...##.",
        "",
        "Tile 3079:",
        "#.#.#####.",
        ".#..######",
        "..#.......",
        "######....",
        "####.#..#.",
        ".#...#.##.",
        "#.#####.##",
        "..#.###...",
        "..#.......",
        "..#.###...",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=20899048083289,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=273,
    )
    part_2.submit_answer()

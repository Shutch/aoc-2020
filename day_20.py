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
    for y in range(10):
        for x in range(10):
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
            edges.append(
                {
                    "edge": edge,
                    "orientation": 0,
                    "hor_flipped": False,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": edge,
                    "orientation": 180,
                    "hor_flipped": False,
                    "vert_flipped": True,
                }
            )
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 0,
                    "hor_flipped": True,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 180,
                    "hor_flipped": True,
                    "vert_flipped": True,
                }
            )

            # bottom edge
            edge = []
            for x in range(9, -1, -1):
                edge.append(tiles[tile_id][(x, 9)])
            edges.append(
                {
                    "edge": edge,
                    "orientation": 180,
                    "hor_flipped": False,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": edge,
                    "orientation": 0,
                    "hor_flipped": False,
                    "vert_flipped": True,
                }
            )
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 180,
                    "hor_flipped": True,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 0,
                    "hor_flipped": True,
                    "vert_flipped": True,
                }
            )

            # right edge
            edge = []
            for y in range(10):
                edge.append(tiles[tile_id][(9, y)])
            edges.append(
                {
                    "edge": edge,
                    "orientation": 90,
                    "hor_flipped": False,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": edge,
                    "orientation": 270,
                    "hor_flipped": True,
                    "vert_flipped": False,
                }
            )
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 90,
                    "hor_flipped": False,
                    "vert_flipped": True,
                }
            )
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 270,
                    "hor_flipped": True,
                    "vert_flipped": True,
                }
            )

            # left edge
            edge = []
            for y in range(9, -1, -1):
                edge.append(tiles[tile_id][(0, y)])
            edges.append(
                {
                    "edge": edge,
                    "orientation": 270,
                    "hor_flipped": False,
                    "vert_flipped": False,
                }
            )
            edges.append(
                {
                    "edge": edge,
                    "orientation": 90,
                    "hor_flipped": True,
                    "vert_flipped": False,
                }
            )
            flipped_edge = edge.copy()
            flipped_edge.reverse()
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 270,
                    "hor_flipped": False,
                    "vert_flipped": True,
                }
            )
            edges.append(
                {
                    "edge": flipped_edge,
                    "orientation": 90,
                    "hor_flipped": True,
                    "vert_flipped": True,
                }
            )

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
            "hor_flipped": False,
            "vert_flipped": False,
        }
        tile_locations[starting_tile_id] = current_tile
        while len(unset_tile_ids) > 0:
            for index in range(len(set_tile_ids) - 1, -1, -1):
                current_tile_id = set_tile_ids[index]
                current_tile = tile_locations[current_tile_id]
                logging.debug(f"Now matching {current_tile_id}")
                for edge in tile_edges[current_tile_id]:
                    if (
                        edge["hor_flipped"] == current_tile["hor_flipped"]
                        and edge["vert_flipped"] == current_tile["vert_flipped"]
                    ):
                        for matching_tile_id in unset_tile_ids:
                            for matching_edge in tile_edges[matching_tile_id]:
                                if edge["edge"] == matching_edge["edge"]:
                                    logger.debug(
                                        f"\nmatch {current_tile_id} ({edge})\n with {matching_tile_id} ({matching_edge})"
                                    )

                                    orientation = (
                                        edge["orientation"]
                                        - matching_edge["orientation"]
                                        + current_tile["orientation"]
                                        + 180
                                    ) % 360

                                    if (
                                        edge["orientation"]
                                        + current_tile["orientation"]
                                    ) % 360 == 0:
                                        coords = (
                                            current_tile["coords"][0],
                                            current_tile["coords"][1] + 1,
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
                                            current_tile["coords"][1] - 1,
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

                                    hor_flipped = matching_edge["hor_flipped"]
                                    vert_flipped = matching_edge["vert_flipped"]
                                    tile_locations[matching_tile_id] = {
                                        "coords": coords,
                                        "orientation": orientation,
                                        "hor_flipped": hor_flipped,
                                        "vert_flipped": vert_flipped,
                                    }
                                    logger.debug(set_tile_ids)
                                    logger.debug(unset_tile_ids)
                                    logger.debug(matching_tile_id)
                                    set_tile_ids.append(matching_tile_id)
                                    unset_tile_ids.remove(matching_tile_id)
                                    pprint.pprint(tile_locations)
                                    break
                del set_tile_ids[index]
                logger.debug(set_tile_ids)
                logger.debug(unset_tile_ids)
        logger.debug(unset_tile_ids)

        sea_monster = [
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   ",
        ]


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

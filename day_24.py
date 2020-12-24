#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        # https://www.redblobgames.com/grids/hexagons/
        directions = {
            "e": (1, -1, 0),
            "se": (0, -1, 1),
            "sw": (-1, 0, 1),
            "w": (-1, 1, 0),
            "nw": (0, +1, -1),
            "ne": (1, 0, -1),
        }

        # starts white (0), and flips to black (1)
        tiles = {(0, 0, 0): 0}
        for steps in inp:
            index = 0
            current_tile = (0, 0, 0)
            while index < len(steps):
                # check the single char directions
                if steps[index] in ["e", "w"]:
                    step = steps[index]
                    index += 1
                else:
                    step = steps[index : index + 2]
                    index += 2
                next_coords = (
                    current_tile[0] + directions[step][0],
                    current_tile[1] + directions[step][1],
                    current_tile[2] + directions[step][2],
                )
                logger.debug(f"Moved {step}, on {next_coords}")
                current_tile = next_coords
            current_tile_color = tiles.get(current_tile, 0)
            tiles[current_tile] = 1 if current_tile_color == 0 else 0
            logger.debug(f"Flipped {current_tile} to {current_tile_color}")
        logger.debug(tiles)
        black_tiles = sum(tiles.values())
        logger.debug(black_tiles)
        return black_tiles


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        # https://www.redblobgames.com/grids/hexagons/
        directions = {
            "e": (1, -1, 0),
            "se": (0, -1, 1),
            "sw": (-1, 0, 1),
            "w": (-1, 1, 0),
            "nw": (0, +1, -1),
            "ne": (1, 0, -1),
        }

        # starts white (0), and flips to black (1)
        tiles = {(0, 0, 0): 0}
        for steps in inp:
            index = 0
            current_tile = (0, 0, 0)
            while index < len(steps):
                # check the single char directions
                if steps[index] in ["e", "w"]:
                    step = steps[index]
                    index += 1
                else:
                    step = steps[index : index + 2]
                    index += 2
                next_coords = (
                    current_tile[0] + directions[step][0],
                    current_tile[1] + directions[step][1],
                    current_tile[2] + directions[step][2],
                )
                logger.debug(f"Moved {step}, on {next_coords}")
                current_tile = next_coords
            current_tile_color = tiles.get(current_tile, 0)
            tiles[current_tile] = 1 if current_tile_color == 0 else 0
            logger.debug(f"Flipped {current_tile} to {current_tile_color}")
        logger.debug(tiles)

        # days
        days = 100
        for day in range(1, days + 1):
            new_tiles = tiles.copy()
            black_tiles = [coords for coords, color in tiles.items() if color == 1]

            # checking black tiles
            for tile in black_tiles:
                black_black_tiles = 0
                for direction, coords in directions.items():
                    check_coords = (
                        tile[0] + coords[0],
                        tile[1] + coords[1],
                        tile[2] + coords[2],
                    )
                    if tiles.get(check_coords, 0) == 1:  # black surrounding tile
                        black_black_tiles += 1
                    else:  # white surrounding tile
                        # checking surrounding white tiles
                        white_black_tiles = 0
                        for surrounding_tile in black_tiles:
                            if (
                                (abs(surrounding_tile[0] - check_coords[0]) <= 1)
                                and (abs(surrounding_tile[1] - check_coords[1]) <= 1)
                                and (abs(surrounding_tile[2] - check_coords[2]) <= 1)
                            ):
                                white_black_tiles += 1

                        if white_black_tiles == 2:
                            # logger.debug(f"Day {day}, Flipped {check_coords} to black")
                            new_tiles[check_coords] = 1

                if black_black_tiles == 0 or black_black_tiles > 2:
                    # logger.debug(f"Day {day}, Flipped {tile} to white")
                    new_tiles[tile] = 0

            tiles = new_tiles
            logger.debug(f"Day {day}")

        logger.debug(tiles)

        black_tiles = sum(tiles.values())
        logger.debug(black_tiles)
        return black_tiles


if __name__ == "__main__":
    day_number = 24
    test_input = [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=10,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=2208,
    )
    part_2.submit_answer()

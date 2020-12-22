#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")
logger.setLevel(logging.INFO)


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        line_num = 1
        line = inp[line_num]
        player_1 = []
        while line != "":
            player_1.append(int(line))
            line_num += 1
            line = inp[line_num]

        line_num += 2
        player_2 = []
        for line in inp[line_num:]:
            player_2.append(int(line))

        logger.debug(player_1)
        logger.debug(player_2)

        turns = 1
        while len(player_1) > 0 and len(player_2) > 0:
            card_1 = player_1.pop(0)
            card_2 = player_2.pop(0)
            if card_1 > card_2:
                player_1.append(card_1)
                player_1.append(card_2)
            elif card_1 < card_2:
                player_2.append(card_2)
                player_2.append(card_1)
            turns += 1

        logger.debug(player_1)
        logger.debug(player_2)

        winner = player_1 if len(player_1) > 0 else player_2
        total_score = 0
        for index, card in enumerate(winner[::-1]):
            total_score += (index + 1) * card

        logger.debug(total_score)
        return total_score


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        line_num = 1
        line = inp[line_num]
        player_1 = []
        while line != "":
            player_1.append(int(line))
            line_num += 1
            line = inp[line_num]

        line_num += 2
        player_2 = []
        for line in inp[line_num:]:
            player_2.append(int(line))

        logger.debug(player_1)
        logger.debug(player_2)

        winner = game(player_1, player_2)

        logger.debug(winner)
        logger.debug(player_1)
        logger.debug(player_2)

        winner = player_1 if len(player_1) > 0 else player_2
        total_score = 0
        for index, card in enumerate(winner[::-1]):
            total_score += (index + 1) * card

        logger.debug(total_score)
        return total_score


def game(player_1, player_2):
    turns = 1
    previous_rounds = []
    # logger.debug(f"New Recursive Game")
    while len(player_1) > 0 and len(player_2) > 0:
        logger.debug(f"Player 1's deck: {player_1}")
        logger.debug(f"Player 2's deck: {player_2}")
        # repeat cards rule
        if (player_1, player_2) in previous_rounds:
            logger.debug("Player 1 wins on duplication rule")
            return 1
        previous_rounds.append((player_1.copy(), player_2.copy()))

        # round
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        logger.debug(f"Player 1 plays: {card_1}")
        logger.debug(f"Player 2 plays: {card_2}")
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            winner = game(player_1[:card_1], player_2[:card_2])
            if winner == 1:
                logger.debug(f"Player 1 wins round {turns}")
                player_1.append(card_1)
                player_1.append(card_2)
            else:
                logger.debug(f"Player 2 wins round {turns}")
                player_2.append(card_2)
                player_2.append(card_1)
        elif card_2 < card_1:
            logger.debug(f"Player 1 wins round {turns}")
            player_1.append(card_1)
            player_1.append(card_2)
        elif card_1 < card_2:
            logger.debug(f"Player 2 wins round {turns}")
            player_2.append(card_2)
            player_2.append(card_1)
        turns += 1
    winner = 1 if len(player_1) > 0 else 2
    logger.debug(f"Player {winner} wins")
    return winner


if __name__ == "__main__":
    day_number = 22
    test_input = [
        "Player 1:",
        "9",
        "2",
        "6",
        "3",
        "1",
        "",
        "Player 2:",
        "5",
        "8",
        "4",
        "7",
        "10",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=306,
    )
    part_1.submit_answer()

    test_input = [
        "Player 1:",
        "30",
        "42",
        "25",
        "7",
        "29",
        "1",
        "16",
        "50",
        "11",
        "40",
        "4",
        "41",
        "3",
        "12",
        "8",
        "20",
        "32",
        "38",
        "31",
        "2",
        "44",
        "28",
        "33",
        "18",
        "10",
        "",
        "Player 2:",
        "36",
        "13",
        "46",
        "15",
        "27",
        "45",
        "5",
        "19",
        "39",
        "24",
        "14",
        "9",
        "17",
        "22",
        "37",
        "47",
        "43",
        "21",
        "6",
        "35",
        "23",
        "48",
        "34",
        "26",
        "49",
    ]
    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=34771,
    )
    part_2.submit_answer()

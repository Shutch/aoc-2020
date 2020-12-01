#!/bin/python
import requests
import argparse
import bs4  # type:ignore

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


def get_prompt(day_number: int) -> None:
    url: str = base_url + str(day_number)
    r = requests.get(url)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    prompt: str = soup.article.text
    print(prompt)


def submit_answer(day_number: int) -> None:
    url: str = base_url + str(day_number) + answer_suffix
    # POST with answer as value


def get_input(day_number: int) -> None:
    url: str = base_url + str(day_number) + input_suffix


def get_answer_response(day_number: int) -> None:
    pass


def test_pass() -> None:
    assert True


def main() -> None:
    # aoc prompt 1
    # aoc test 1
    # aoc answer 1
    parser = argparse.ArgumentParser(
        description="CLI tool for interacting with Advent of Code 2020"
    )


if __name__ == "__main__":
    main()

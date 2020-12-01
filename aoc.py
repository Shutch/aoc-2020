#!/bin/python
import requests
import argparse
import bs4  # type:ignore
import textwrap
import click
import secrets
from typing import List

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


def get_prompt(day_number: int) -> str:
    url: str = base_url + str(day_number)
    r = requests.get(url)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    prompt: str = soup.article.text
    return prompt


def submit_answer(day_number: int, answer: int) -> None:
    # check to see if test passes

    # submit answer
    url: str = base_url + str(day_number) + answer_suffix
    data = {"level": day_number, "answer": answer}
    r = requests.post(url, data=data)

    # Figure out if it's right or wrong
    # span class="day-success" or "That's the right answer!"
    # "That's not the right answer"


def get_input(day_number: int) -> List[str]:
    cookie = secrets.cookie
    url: str = base_url + str(day_number) + input_suffix
    r = requests.get(url, cookies=cookie)
    return r.text.split()


def get_answer_response(day_number: int) -> None:
    pass


def test_pass() -> None:
    assert True


def print_response(resp: str) -> None:
    wrapper: textwrap.TextWrapper = textwrap.TextWrapper(
        width=88, break_long_words=False, replace_whitespace=False
    )
    wrapped_resp: List[str] = wrapper.wrap(resp)
    for line in wrapped_resp:
        print(line)


def main() -> None:
    # aoc prompt 1
    # aoc test 1
    # aoc answer 1 1234
    pass


if __name__ == "__main__":
    main()

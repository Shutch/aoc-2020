#!/bin/python
import re
import pprint
import textwrap
import requests
import bs4  # type:ignore
import click
import secrets
from typing import List, Any

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


def get_prompt(day_number: int) -> str:
    url: str = base_url + str(day_number)
    cookie = secrets.cookie
    r = requests.get(url, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    articles: List[str] = [article.text for article in soup.find_all("article")]
    full_article: str = "\n".join(articles)
    formatted_article: str = re.sub(r"(---.*---)", r"\1\n", full_article)
    return formatted_article


def submit_answer(day_number: int, answer: int) -> None:
    # check to see if test passes

    # submit answer
    url: str = base_url + str(day_number) + answer_suffix
    cookie = secrets.cookie
    data = {"level": day_number, "answer": answer}
    r = requests.post(url, data=data, cookies=cookie)

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
    # Passing test to make pytest happy
    assert True


def print_response(resp: Any) -> None:
    if type(resp) == str:
        wrapper: textwrap.TextWrapper = textwrap.TextWrapper(
            width=88, break_long_words=False, replace_whitespace=False
        )
        wrapped_resp: List[str] = wrapper.wrap(resp)
        for line in wrapped_resp:
            print(line)
    else:
        pprint.pprint(resp, compact=True)


def convert_str_list(l: List[str], t: Any) -> List[Any]:
    return [t(value) for value in l]


def main() -> None:
    # aoc prompt 1
    # aoc test 1
    # aoc answer 1 1234
    print_response(get_input(1))


if __name__ == "__main__":
    main()

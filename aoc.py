#!/bin/python
import re
import pprint
import textwrap
import importlib
import requests
import bs4  # type:ignore
import click
import secrets
from typing import List, Any, Dict

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


def get_status() -> str:
    url: str = "https://adventofcode.com/"
    cookie = secrets.cookie
    r = requests.get(url, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    days: List[bs4.element.Tag] = soup.find_all(
        ["a", "span"], {"class": re.compile("calendar-day[0-9]+")}
    )
    for day in days:
        label: str = day.attrs.get("aria-label")
        if label is not None and "two star" in label:  # Remove the second star
            pass
        elif label is not None and "one star" in label:  # remove the first star
            day.find("span", {"class": "calendar-mark-complete"}).contents[
                0
            ].replace_with(" ")
        elif label is not None and "star" not in label:
            day.find("span", {"class": "calendar-mark-complete"}).contents[
                0
            ].replace_with(" ")
            day.find("span", {"class": "calendar-mark-verycomplete"}).contents[
                0
            ].replace_with(" ")
    full_status: str = "\n".join([day.text for day in days])
    return full_status


def get_prompt(day_number: int) -> str:
    url: str = base_url + str(day_number)
    cookie = secrets.cookie
    r = requests.get(url, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    articles: List[str] = [article.text for article in soup.find_all("article")]
    full_article: str = "\n".join(articles)
    formatted_article: str = re.sub(r"(---.*---)", r"\1\n", full_article)
    return formatted_article


def submit_answer(day_number: int, answer: int) -> bool:
    # submit answer
    url: str = base_url + str(day_number) + answer_suffix
    cookie = secrets.cookie
    data = {"level": day_number, "answer": answer}
    r = requests.post(url, data=data, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    article: str = soup.find("article").text
    if "That's the right answer!" in article:
        return True
    elif "That's not the right answer;" in article:
        return False
    else:
        raise ValueError(f"Unknown answer respone: {article}")


def get_input(day_number: int) -> List[str]:
    cookie = secrets.cookie
    url: str = base_url + str(day_number) + input_suffix
    r = requests.get(url, cookies=cookie)
    return r.text.split("\n")


def test_pass() -> None:
    # Passing test to make pytest happy
    assert True


def convert_str_list(l: List[str], t: Any) -> List[Any]:
    return [t(value) for value in l]


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("day", type=int)
def prompt(day: int) -> None:
    resp: str = get_prompt(day)
    if type(resp) == str:
        wrapper: textwrap.TextWrapper = textwrap.TextWrapper(
            width=88, break_long_words=False, replace_whitespace=False
        )
        wrapped_resp: List[str] = wrapper.wrap(resp)
        for line in wrapped_resp:
            print(line)


@main.command()
@click.argument("day", type=int)
@click.argument("answer", type=int)
def answer(day: int, answer: int) -> None:
    resp: bool = submit_answer(day, answer)
    if resp:
        print("Right answer")
    else:
        print("Wrong answer")


@main.command()
@click.argument("day", type=int)
@click.option(
    "-f", "--file", "file_name", default="", type=str, help="Output to file name"
)
def input(day: int, file_name: str = "") -> None:
    resp: List[str] = get_input(day)
    if file_name == "":
        pprint.pprint(resp, compact=True)
    else:
        with open(file_name, "w") as f:
            for line in resp:
                f.write(str(line) + "\n")


@main.command()
def status() -> None:
    resp: str = get_status()
    print(resp)


if __name__ == "__main__":
    main()

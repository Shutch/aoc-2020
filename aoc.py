#!/usr/bin/env python
import re
import requests
import bs4  # type:ignore
import secrets
import time
import os
import pickle
from abc import ABC, abstractmethod
from typing import List, Any

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


class Part(ABC):
    def __init__(
        self,
        day_number: int,
        test_input: List[str],
        test_answer: int,
        debug: bool = True,
    ) -> None:
        self.day_number: int = day_number
        self.test_input: List[str] = test_input
        self.test_answer: int = test_answer
        self.real_input: List[str] = get_input(day_number, save_input=True)
        self.debug: bool = debug

    @staticmethod
    @abstractmethod
    def logic(inp: List[str]) -> int:
        raise NotImplementedError("Implement logic method")

    def test(self) -> bool:
        start = time.time()
        ans = self.logic(self.test_input)
        elapsed_time = time.time() - start
        if self.debug:
            outcome: str = "PASSED" if ans == self.test_answer else "FAILED"
            print(
                f"{outcome},    SB: {self.test_answer},    IS: {ans},    ET: {elapsed_time:.3f} s"
            )
        return True if ans == self.test_answer else False

    def submit_answer(self) -> None:
        if self.test():
            ans: int = self.logic(self.real_input)
            resp: bool = submit_answer(self.day_number, ans)
            if self.debug:
                if resp:
                    print(f"Right answer ({ans})")
                else:
                    print(f"Wrong answer ({ans})")


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


def get_input(day_number: int, save_input: bool = False) -> List[str]:
    # Check to see if it's locally stored
    input_file_name = f"./inputs/day_{day_number}_input.p"
    input_lines: List[str] = []
    if os.path.isfile(input_file_name):
        with open(input_file_name, "rb") as f:
            input_lines = pickle.load(f)
    else:  # gathering the input from the aoc website
        cookie = secrets.cookie
        url: str = base_url + str(day_number) + input_suffix
        r = requests.get(url, cookies=cookie)
        input_lines = r.text.split("\n")
        if save_input:
            with open(input_file_name, "wb") as f:
                pickle.dump(input_lines, f)
    return input_lines


def convert_str_list(input_list: List[str], output_type: Any) -> List[Any]:
    return [output_type(value) for value in input_list]

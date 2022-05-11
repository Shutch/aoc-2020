#!/usr/bin/env python
import re
import requests
import bs4  # type:ignore
import secrets
import time
import os
import logging
from abc import ABC, abstractmethod
from typing import List, Any

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


class Part(ABC):
    def __init__(
        self,
        day_number: int,
        part: int,
        test_input: List[str],
        test_answer: int,
        debug: bool = True,
    ) -> None:
        self.day_number: int = day_number
        self.part: int = part
        self.test_input: List[str] = test_input
        self.test_answer: int = test_answer
        self.real_input: List[str] = get_input(day_number, save_input=True)

        logging_level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=logging_level)
        self.logger = logging.getLogger("Part")
        logging.getLogger("requests").setLevel(logging.INFO)  # disable requests logger
        logging.getLogger("urllib3").setLevel(logging.INFO)  # disable requests logger

    @staticmethod
    @abstractmethod
    def logic(inp: List[str]) -> int:
        raise NotImplementedError("Implement logic method")

    def test(self) -> bool:
        start = time.time()
        ans = self.logic(self.test_input)
        elapsed_time = time.time() - start
        passed: bool = True if ans == self.test_answer else False
        self.logger.info(f"Part {self.part}:")
        self.logger.info(
            (
                f"Test: {'PASSED' if passed else 'FAILED'},    "
                f"SB: {self.test_answer},    "
                f"IS: {ans},    ET: {elapsed_time:.3f} s"
            )
        )
        return passed

    def submit_answer(self) -> None:
        # only submit if tests pass
        if self.test():
            # check if answer needs to be submitted
            url: str = base_url + str(self.day_number)
            cookie = secrets.cookie
            r = requests.get(url, cookies=cookie)
            soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
            input_tag = soup.find("input")
            if input_tag is not None:
                requested_part = int(input_tag["value"])
                if requested_part == self.part:
                    start = time.time()
                    ans: int = self.logic(self.real_input)
                    elapsed_time = time.time() - start
                    resp: bool = submit_answer(self.day_number, self.part, ans)
                    self.logger.info(
                        (
                            f"Real: {'PASSED' if resp else 'FAILED'},    "
                            f"ANS: {ans},    ET: {elapsed_time:.3f} s"
                        )
                    )
                else:
                    self.logger.info(
                        (
                            "No answer entered. Input form requesting part "
                            f"{requested_part}"
                        )
                    )
            else:
                self.logger.info("No input form on prompt page found")


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


def submit_answer(day_number: int, level: int, answer: int) -> bool:
    # submit answer
    url: str = base_url + str(day_number) + answer_suffix
    cookie = secrets.cookie
    data = {"level": level, "answer": answer}
    r = requests.post(url, data=data, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    article: str = soup.find("article").text
    if "That's the right answer" in article:
        return True
    elif "That's not the right answer" in article:
        return False
    else:
        raise ValueError(f"Unknown answer respone: {article}")

def test_post(day_number: int, level: int, answer: int) -> bool:
    # submit answer
    url: str = base_url + str(day_number) + answer_suffix
    url: str = "https://httpbin.org/post"
    cookie = secrets.cookie
    data = {"level": level, "answer": answer}
    r = requests.post(url, data=data, cookies=cookie)
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")
    print(soup.text)


def get_input(day_number: int, save_input: bool = False) -> List[str]:
    # Check to see if it's locally stored
    input_file_name = f"./inputs/day_{day_number}_input.txt"
    input_lines: List[str] = []
    if os.path.isfile(input_file_name):
        with open(input_file_name, "r") as f:
            # inputs read from a file have one blank string at the end
            input_lines = f.read().split("\n")[:-1]
    else:  # gathering the input from the aoc website
        cookie = secrets.cookie
        url: str = base_url + str(day_number) + input_suffix
        r = requests.get(url, cookies=cookie)
        # inputs read from the website have one blank string at the end
        input_lines = r.text.split("\n")[:-1]
        if save_input:  # if the flag is set, save it to a file as plain-text
            with open(input_file_name, "w") as f:
                for line in input_lines:
                    f.write(line + "\n")
    return input_lines


def convert_str_list(input_list: List[str], output_type: Any) -> List[Any]:
    return [output_type(value) for value in input_list]

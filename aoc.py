import requests
from bs4 import BeautifulSoup

base_url = "https://adventofcode.com/2020/day/"
input_suffix = "/input"
answer_suffix = "/answer"


def get_prompt(day_number: int):
    url: str = base_url + str(day_number)
    soup = BeautifulSoup(r.text, "html.parser")


def submit_answer(day_number: int):
    url: str = base_url + str(day_number) + answer_suffix
    # POST with answer as value


def get_input(day_number: int):
    url: str = base_url + str(day_number) + input_suffix


def get_answer_response(day_number: int):
    pass

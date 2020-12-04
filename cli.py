import aoc
import click
import textwrap
import pprint
from typing import List


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("day", type=int)
def prompt(day: int) -> None:
    resp: str = aoc.get_prompt(day)
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
    resp: bool = aoc.submit_answer(day, answer)
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
    resp: List[str] = aoc.get_input(day)
    if file_name == "":
        pprint.pprint(resp, compact=True)
    else:
        with open(file_name, "w") as f:
            for line in resp:
                f.write(str(line) + "\n")


@main.command()
def status() -> None:
    resp: str = aoc.get_status()
    print(resp)


if __name__ == "__main__":
    main()

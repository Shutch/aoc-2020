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
    print(resp)


@main.command()
@click.argument("day", type=int)
@click.argument("part", type=int)
@click.argument("answer", type=int)
def answer(day: int, part: int, answer: int) -> None:
    resp: bool = aoc.submit_answer(day, part, answer)
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

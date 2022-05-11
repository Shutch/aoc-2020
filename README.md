# Advent of Code 2020
[Advent of Code](https://adventofcode.com/2020) is an annual programming competition that
starts on December 1st and runs until December 25th. Each day at midnight Eastern Time a
new problem is released. The problems take the form of several paragraphs of Christmas
exposition that describe the problem, as well as an example input and the expected output.

The input and answer to each puzzle is unique to each user (an account is required to submit answers)
and after a successful answer is submitted a second, more difficult problem is also unlocked which
builds on the first part. Each answer is either an integer or a string so there is no chance of precision
errors.

The days are not related to each other and can be completed in any order once they are unlocked.

## AOC Library
Located in `aoc.py`, this library uses the Requests and BeautifulSoup4 libraries to interact with the
Advent of Code site. It contains functions for getting a problem's status, retrieving the input, and 
submitting answers. It also caches inputs locally in the `inputs/` folder.

The library looks for a `secrets.py` file in the project directory which contains a dictionary called cookie.
The user's cookie (after logging in) should be stored in the value of the key 'session'
```
cookie = {"session": "yourcookiegoeshereyoucanretrieveitfromyourbrowseronceyoulogin"}
```

When submitting an answer, the AOC library will run the test input located in the day's python file and check the answer
against the given answer from the prompt. If it matches, it will run the real input and submit the answer to the AOC website.

## Command Line Interface
Located in `cli.py`, the command line interface uses the Click and AOC library to create a basic CLI
to interact with the AOC website and test code locally.

```
python cli.py prompt 20
```

Any prompt or input will be printed to the console with formatting preserved.

## Individual Days

Each day has an associated python file, created from the `day.py` template file.

The test input and expected output from the problem description is manually copied into the file in the `test_input` and `test_answer`
arguments. Each part has a class that inherits the `Part` class from the AOC library and static function that will accept the puzzle
input and return the puzzle output.

## Pre-commit Hooks

Some pre-commit hooks can be installed that run Black and MyPy on the repository.

import os
import typing

import requests


def no_token():
    raise FileNotFoundError(
        f"Could not find token, please follow https://github.com/isaa-ctaylor/aoc-helper/blob/master/README.md#setup to add it"
    )


TOKEN: typing.Optional[str] = None
try:
    with open(os.path.expanduser("~/.aoc/.token"), "r") as f:
        TOKEN = f.read()
except FileNotFoundError:
    no_token()

if not TOKEN:
    no_token()


def get_input(year: int, day: int):
    """
    Get your input for the given year and day
    """
    if os.path.exists(os.path.expanduser(f"~/.aoc/{year}/{day}")):
        with open(os.path.expanduser(f"~/.aoc/{year}/{day}"), "r") as f:
            return f.read()

    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": TOKEN}  # type: ignore
    )
    if r.status_code == 400:
        raise Exception(
            f"Request failed, please check your token (https://github.com/isaa-ctaylor/aoc-helper/blob/master/README.md#setup)"
        )
    if r.status_code == 404:
        raise Exception(
            f"Input not available, are you sure the day is correct and the puzzle is unlocked?"
        )
    if r.status_code == 200:
        ret = r.text

        if not os.path.exists(os.path.expanduser(f"~/.aoc/{year}")):
            os.mkdir(os.path.expanduser(f"~/.aoc/{year}"))

        with open(os.path.expanduser(f"~/.aoc/{year}/{day}"), "w") as f:
            f.write(ret)
        return ret
    else:
        raise Exception(r"An error occured ¯\_(ツ)_/¯")


def submit(year: int, day: int, part: int, answer: str):
    r = requests.post(
        f"https://adventofcode.com/{year}/day/{day}/answer",
        cookies={"session": TOKEN},  # type: ignore
        data={"level": part, "answer": answer},
    )
    if r.status_code == 400:
        raise Exception(
            f"Request failed, please check your token (https://github.com/isaa-ctaylor/aoc-helper/blob/master/README.md#setup)"
        )
    if r.status_code == 200:
        print(r.text)

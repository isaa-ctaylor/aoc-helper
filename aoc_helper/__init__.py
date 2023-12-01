import requests
import os

RED = "\x1b[31m"
BOLD = "\x1b[1m"
RESET = "\x1b[0m"

def no_token():
    print(f"{BOLD}{RED}Could not find token, please follow https://github.com/isaa-ctaylor/aoc-helper/blob/master/README.md#setup to add it{RESET}")
    os._exit(0)

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
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": TOKEN})
    if r.status_code == 400:
        print(f"{BOLD}{RED}Request failed, please check your token (https://github.com/isaa-ctaylor/aoc-helper/blob/master/README.md#setup){RESET}")
    if r.status_code == 200:
        return r.text
    else:
        raise Exception("An error occured ¯\_(ツ)_/¯")

if __name__ == "__main__":
    print(get_input(2023, 1))
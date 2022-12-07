# aoc_template.py


import pathlib

import sys

import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# WARNING
# this turns binary strings ex. "0011" to ints by default
# making rr(), read impossible as a string

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))


def parse(puzzle_input):

    """Parse input."""
    vals = []
    for line in puzzle_input.splitlines():
        vals.append(line)
    return vals


def part1(data):

    """Solve part 1."""

def part2(data):

    """Solve part 2."""


def solve(puzzle_input):

    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)

    solution1 = part1(data)

    solution2 = part2(data)


    return solution1, solution2


if __name__ == "__main__":

    for path in sys.argv[1:]:

        print(f"{path}:")

        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)

        print("\n".join(str(solution) for solution in solutions))

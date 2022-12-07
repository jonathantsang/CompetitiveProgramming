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
    # A rock
    # B paper
    # C scissors

    # X rock 1
    # Y paper 2
    # Z scissors 3

    score = 0

    for game in data:
        opp,you = game.split()
        if you == 'X':
            score += 1
            if opp == 'A':
                score += 3
            elif opp == 'C':
                score += 6
        if you == 'Y':
            score += 2
            if opp == 'A':
                score += 6
            elif opp == 'B':
                score += 3
        if you == 'Z':
            score += 3
            if opp == 'B':
                score += 6
            elif opp == 'C':
                score += 3
    return score



def part2(data):

    """Solve part 2."""
    # A rock
    # B paper
    # C scissors

    # X lose outcome
    # Y draw outcome
    # Z win outcome
    score = 0

    for game in data:
        opp,outcome = game.split()
        if outcome == 'X':
            if opp == 'A':
                score += 3
            elif opp == 'B':
                score += 1
            else:
                score += 2
        if outcome == 'Y':
            score += 3
            if opp == 'A':
                score += 1
            elif opp == 'B':
                score += 2
            else:
                score += 3
        if outcome == 'Z':
            score += 6
            if opp == 'A':
                score += 2
            elif opp == 'B':
                score += 3
            else:
                score += 1
    return score


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

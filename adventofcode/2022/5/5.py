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
    cols = 9
    ops = False
    stacks = [[] for _ in range(cols)]
    ans = []
    for line in data:
        if ops == False and line[:4] == "move":
            ops = True
            for i in range(cols):
                stacks[i] = stacks[i][::-1]
        if ops == True and line[:4] == "move":
            w1,amt,w2,orig,w3,dest = line.split()

            amt=int(amt)
            orig=int(orig)-1
            dest=int(dest)-1
            # FIFO
            for j in range(amt):
                stacks[dest].append(stacks[orig].pop())
        else:
            for i in range(cols):
                if i*4+1 >= len(line):
                    break
                letter = line[i*4+1]
                if letter != ' ' and letter != '.':
                    stacks[i].append(letter)

    for i in range(cols):
        ans.append(stacks[i][-1])

    return ''.join(ans)

def part2(data):

    """Solve part 2."""
    cols = 9
    ops = False
    stacks = [[] for _ in range(cols)]
    ans = []
    for line in data:
        if ops == False and line[:4] == "move":
            ops = True
            for i in range(cols):
                stacks[i] = stacks[i][::-1]
        if ops == True and line[:4] == "move":
            w1,amt,w2,orig,w3,dest = line.split()

            amt=int(amt)
            orig=int(orig)-1
            dest=int(dest)-1

            # FILO
            temp = []
            for j in range(amt):
                temp.append(stacks[orig].pop())
            temp=temp[::-1]
            stacks[dest].extend(temp)

        else:
            for i in range(cols):
                if i*4+1 >= len(line):
                    break
                letter = line[i*4+1]
                if letter != ' ' and letter != '.':
                    stacks[i].append(letter)

    for i in range(cols):
        ans.append(stacks[i][-1])

    return ''.join(ans)




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

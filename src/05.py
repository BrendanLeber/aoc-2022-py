# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 5: Supply Stacks."""

import argparse
import pdb
import traceback
from copy import deepcopy

from more_itertools import grouper


def parse_input(text: str):
    sections = text.split("\n\n")

    towers = sections[0].split("\n")
    size = len(towers[-1].split())
    towers = towers[:-1]
    stacks = [[] for _ in range(size)]
    for row in towers:
        for idx, box in enumerate(grouper(row, 4, fillvalue=" ")):
            if box[1] == " ":
                continue
            stacks[idx].insert(0, box[1])

    moves = []
    for instruction in sections[1].split("\n"):
        parts = instruction.split()
        moves.append((int(parts[1]), int(parts[3]), int(parts[5])))

    return (stacks, moves)


def part_1(puzzle):
    stacks = deepcopy(puzzle[0])
    for count, src, dest in puzzle[1]:
        for _ in range(count):
            box = stacks[src - 1].pop()
            stacks[dest - 1].append(box)

    tops = []
    for stack in stacks:
        tops.append(stack[-1])

    return "".join(tops)


def part_2(puzzle):
    stacks = deepcopy(puzzle[0])
    for count, src, dest in puzzle[1]:
        boxes = stacks[src - 1][-count:]
        stacks[src - 1] = stacks[src - 1][: len(stacks[src - 1]) - count]
        stacks[dest - 1].extend(boxes)

    tops = []
    for stack in stacks:
        tops.append(stack[-1])

    return "".join(tops)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../examples/05.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r") as inf:
        text = inf.read().strip("\n")

    try:
        puzzle = parse_input(text)
        print(f"{part_1(puzzle)} (VQZNJMWTR)")
        print(f"{part_2(puzzle)} (NLCDCLVMQ)")
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

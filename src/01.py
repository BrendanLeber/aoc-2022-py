# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 1: Calorie Counting."""

import argparse
import pdb
import traceback


def parse_input(text: str):
    blocks = []
    for block in text.split("\n\n"):
        blocks.append(list(map(int, block.split())))
    return blocks


def part_1(elves):
    totals: list[int] = []
    for elf in elves:
        totals.append(sum(elf))
    return max(totals)


def part_2(elves):
    totals: list[int] = []
    for elf in elves:
        totals.append(sum(elf))
    totals.sort(reverse=True)
    return sum(totals[:3])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../inputs/01.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r") as inf:
        text = inf.read().strip()

    try:
        puzzle = parse_input(text)
        print(part_1(puzzle))
        print(part_2(puzzle))
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

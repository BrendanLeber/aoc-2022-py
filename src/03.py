# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 3: Rucksack Reorganizaion."""

import argparse
import pdb
import traceback

from more_itertools import chunked

LETTERS = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def parse_input(text: str):
    return text.split("\n")


def part_1(puzzle):
    priorities = 0
    for rucksack in puzzle:
        left, right = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
        item = set(left).intersection(set(right)).pop()
        priorities += LETTERS.index(item)
    return priorities


def part_2(puzzle):
    priorities = 0
    for groups in chunked(puzzle, 3, strict=True):
        rucksacks = [set(x) for x in groups]
        item = rucksacks[0].intersection(*rucksacks[1:]).pop()
        priorities += LETTERS.index(item)
    return priorities


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../inputs/03.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r") as inf:
        text = inf.read().strip()

    try:
        puzzle = parse_input(text)
        print(f"{part_1(puzzle)} (8072)")
        print(f"{part_2(puzzle)} (2567)")
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

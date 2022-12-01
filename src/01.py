# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 1: Calorie Counting."""

import argparse
import pdb
import traceback


def part_01(elves: list[list[int]]) -> int:
    totals: list[int] = []
    for elf in elves:
        totals.append(sum(elf))
    print(max(totals))


def part_02(elves: list[list[int]]) -> int:
    totals: list[int] = []
    for elf in elves:
        totals.append(sum(elf))
    totals.sort(reverse=True)
    print(sum(totals[:3]))


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
        content = inf.read().strip()

    blocks = []
    for block in content.split("\n\n"):
        blocks.append(list(map(int, block.split())))

    try:
        part_01(blocks)
        part_02(blocks)
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

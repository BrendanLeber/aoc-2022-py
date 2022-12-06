# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 6: Tuning Trouble."""

import argparse
import pdb
import traceback

from more_itertools import sliding_window


def parse_input(text: str):
    return text.strip()


def part_1(puzzle):
    for idx, part in enumerate(sliding_window(puzzle, 4)):
        if len(set(part)) == 4:
            return idx + 4
    return -1


def part_2(puzzle):
    for idx, part in enumerate(sliding_window(puzzle, 14)):
        if len(set(part)) == 14:
            return idx + 14
    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../examples/06.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r") as inf:
        text = inf.read().strip("\n")

    try:
        puzzle = parse_input(text)
        print(f"{part_1(puzzle)} (1582)")
        print(f"{part_2(puzzle)} (3588)")
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

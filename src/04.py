# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 4: Camp Cleanup."""

import argparse
import pdb
import traceback


def parse_input(text: str):
    puzzle = []
    for line in text.split("\n"):
        pairs = line.split(",")
        left = map(int, pairs[0].split("-"))
        right = map(int, pairs[1].split("-"))
        puzzle.append((tuple(left), tuple(right)))
    return puzzle


def part_1(puzzle):
    fully_contained = 0
    for left, right in puzzle:
        if right[0] >= left[0] and right[1] <= left[1]:
            fully_contained += 1
        elif left[0] >= right[0] and left[1] <= right[1]:
            fully_contained += 1
    return fully_contained


def part_2(puzzle):
    partial_overlap = 0
    for pairs in puzzle:
        left, right = sorted(pairs)
        if left[1] >= right[0] or right[0] <= left[1]:
            partial_overlap += 1
    return partial_overlap


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../examples/04.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r") as inf:
        text = inf.read().strip()

    try:
        puzzle = parse_input(text)
        print(f"{part_1(puzzle)} (413)")
        print(f"{part_2(puzzle)} (806)")
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

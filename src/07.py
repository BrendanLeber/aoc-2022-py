# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 7: No Space Left On Device."""

import argparse
import operator
import pdb
import traceback
from dataclasses import dataclass
from typing import Any


@dataclass
class File:
    size: int
    name: str


@dataclass
class Directory:
    name: str
    contents: list[Any]
    parent: Any
    size: int


def get_all_dirs(root, results):
    for item in root.contents:
        if isinstance(item, Directory):
            results.append((item.name, item.size))
            get_all_dirs(item, results)


def sum_dir(fs):
    total = 0
    for item in fs.contents:
        if isinstance(item, Directory):
            total += sum_dir(item)
        else:
            total += item.size
    fs.size = total
    return total


def parse_input(text: str):
    root = Directory("/", [], None, -1)
    current = root
    for line in text.strip().split("\n"):
        if line.startswith("$ cd "):
            name = line[5:]
            if name == "/":
                current = root
            elif name == "..":
                current = current.parent
            else:
                found_dir = None
                for dir in current.contents:
                    if isinstance(dir, File):
                        continue
                    if dir.name == name:
                        found_dir = dir
                        break
                assert found_dir is not None
                current = found_dir
        elif line.startswith("$ ls"):
            continue
        else:
            parts = line.split()
            if parts[0] == "dir":
                current.contents.append(Directory(parts[1], [], current, -1))
            else:
                current.contents.append(File(int(parts[0]), parts[1]))

    sum_dir(root)

    return root


def part_1(puzzle):
    LIMIT = 100_000
    dirs = [("/", puzzle.size)]
    get_all_dirs(puzzle, dirs)
    dirs = [item for item in dirs if item[1] <= LIMIT]
    return sum(dir[1] for dir in dirs)


def part_2(puzzle):
    TOTAL_SPACE = 70_000_000
    FREE_SPACE_NEEDED = 30_000_000
    current_free_space = TOTAL_SPACE - puzzle.size
    amount_needed = FREE_SPACE_NEEDED - current_free_space

    dirs = [("/", puzzle.size)]
    get_all_dirs(puzzle, dirs)
    dirs = [item for item in dirs if item[1] >= amount_needed]
    dirs.sort(key=operator.itemgetter(1))
    return dirs[0][1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../examples/07.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    with open(args.input[0], "r", encoding="utf-8") as inf:
        text = inf.read().strip("\n")

    try:
        puzzle = parse_input(text)
        print(f"{part_1(puzzle)} (1581595)")
        print(f"{part_2(puzzle)} (1544176)")
    except Exception:  # pylint: disable=broad-except
        traceback.print_exc()
        pdb.post_mortem()

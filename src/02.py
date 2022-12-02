# -*- coding: utf-8 -*-
"""Advent of Code 2022 - Day 2: Rock Paper Scissors."""

import argparse
import pdb
import traceback
from enum import Enum


Move = Enum("Move", ["ROCK", "PAPER", "SCISSORS"])
Result = Enum("Result", ["LOSE", "TIE", "WIN"])


def desired_result_to_move(opponent: Move, desired_result: Result) -> Move:
    DESIRED_RESULTS_TO_MOVE: dict[Move, dict[Result, Move]] = {
        Move.ROCK: {
            Result.LOSE: Move.SCISSORS,
            Result.TIE: Move.ROCK,
            Result.WIN: Move.PAPER,
        },
        Move.PAPER: {
            Result.LOSE: Move.ROCK,
            Result.TIE: Move.PAPER,
            Result.WIN: Move.SCISSORS,
        },
        Move.SCISSORS: {
            Result.LOSE: Move.PAPER,
            Result.TIE: Move.SCISSORS,
            Result.WIN: Move.ROCK,
        },
    }
    return DESIRED_RESULTS_TO_MOVE[opponent][desired_result]


def input_to_move(value: str) -> Move:
    INPUT_TO_MOVE: dict[str, Move] = {
        # player moves
        "X": Move.ROCK,
        "Y": Move.PAPER,
        "Z": Move.SCISSORS,
        # opponent moves
        "A": Move.ROCK,
        "B": Move.PAPER,
        "C": Move.SCISSORS,
    }
    return INPUT_TO_MOVE[value]


def input_to_result(result: str) -> Result:
    INPUT_TO_RESULT: dict[str, Result] = {
        "X": Result.LOSE,
        "Y": Result.TIE,
        "Z": Result.WIN,
    }
    return INPUT_TO_RESULT[result]


def score_from_move(move: Move) -> int:
    SCORE_FROM_MOVE: dict[Move, int] = {
        Move.ROCK: 1,
        Move.PAPER: 2,
        Move.SCISSORS: 3,
    }
    return SCORE_FROM_MOVE[move]


def score_from_result(result: Result) -> int:
    SCORE_FROM_RESULT: dict[Result, int] = {
        Result.WIN: 6,
        Result.TIE: 3,
        Result.LOSE: 0,
    }
    return SCORE_FROM_RESULT[result]


def turn_result(player_move: Move, opponent_move: Move) -> Result:
    RESULTS: dict[Move, dict[Move, Result]] = {
        Move.ROCK: {
            Move.ROCK: Result.TIE,
            Move.PAPER: Result.LOSE,
            Move.SCISSORS: Result.WIN,
        },
        Move.PAPER: {
            Move.ROCK: Result.WIN,
            Move.PAPER: Result.TIE,
            Move.SCISSORS: Result.LOSE,
        },
        Move.SCISSORS: {
            Move.ROCK: Result.LOSE,
            Move.PAPER: Result.WIN,
            Move.SCISSORS: Result.TIE,
        },
    }
    return RESULTS[player_move][opponent_move]


def part_01(puzzle: list[tuple[str, str]]) -> int:
    total_score: int = 0
    for oinput, pinput in puzzle:
        opponent = input_to_move(oinput)
        player = input_to_move(pinput)
        result = turn_result(player, opponent)
        score = score_from_move(player) + score_from_result(result)
        total_score += score
    return total_score


def part_02(puzzle: list[tuple[str, str]]) -> int:
    total_score: int = 0
    for oinput, result in puzzle:
        opponent = input_to_move(oinput)
        desired_result = input_to_result(result)
        player = desired_result_to_move(opponent, desired_result)
        score = score_from_move(player) + score_from_result(desired_result)
        total_score += score
    return total_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="*",
        default=["../inputs/02.txt"],
        help="The puzzle input.  (Default: %(default)s)",
    )
    args = parser.parse_args()

    puzzle: list[tuple[str, str]] = []
    with open(args.input[0], "r") as inf:
        for line in inf.readlines():
            puzzle.append(tuple(line.split()))

    try:
        print(part_01(puzzle))
        print(part_02(puzzle))
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()

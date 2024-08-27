#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.nod import nod_logic


def main():
    run_game(nod_logic, "Find the greatest common divisor of given numbers.")


if __name__ == "__main__":
    main()

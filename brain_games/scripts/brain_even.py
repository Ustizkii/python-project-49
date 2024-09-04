#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import even


def main():
    """
    Запускает игру "Проверка на четность"
    """
    run_game(even)


if __name__ == "__main__":
    main()

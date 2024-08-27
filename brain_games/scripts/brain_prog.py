from brain_games.engine import run_game
from brain_games.games.progression import progression_logic


def main():
    run_game(progression_logic, "What number is missing in the progression?")


if __name__ == "__main__":
    main()

from brain_games.engine import run_game
from brain_games.games.prime import prime_logic


def main():
    run_game(prime_logic, "Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


if __name__ == "__main__":
    main()

def run_game(game_module):
    """
    Запускает игру с переданным игровым модулем.
    В качестве аргумента функции передается модуль игры, содержащий игровую
    логику и инструкции.
    Функция выводит вопрос и проверяет правильность ответов игрока.
    Если игрок трижды отвечает правильно, он побеждает.
    Если ответ неверен, игра завершится с выводом правильного ответа.
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.INSTRUCTIONS)

    for _ in range(3):
        question, correct_answer = game_module.game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  "Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

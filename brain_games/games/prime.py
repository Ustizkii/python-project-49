import random

INSTRUCTIONS = "Answer 'yes' if given number is prime. Otherwise answer 'no'"


def is_prime(number):
    """
    Проверяет, является ли число простым.
    Простое число — это число, которое делится только на 1 и на само себя.
    В качестве аргумента функции предается интовое число для проверки.
    Возвращается True, если число простое - иначе False.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def game_logic():
    """
    Генерирует случайное число и проверяет, является ли оно простым.
    Возвращается строка с вопросом в виде числа и правильный ответ ('yes' или 'no').
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer

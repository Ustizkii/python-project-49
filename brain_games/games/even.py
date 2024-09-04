import random

INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Проверяет, является ли число четным.
    В качестве аргумента поступает интовое число для проверки.
    Возвращается True, если число четное - иначе False.
    """
    return number % 2 == 0


def game_logic():
    """
    Генерирует случайное число от 1 до 100 и определяет правильный ответ.
    Возвращается вопрос в виде строки и правильный ответ ('yes' или 'no').
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer

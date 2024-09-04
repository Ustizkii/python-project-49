import random

INSTRUCTIONS = "What number is missing in the progression?"


def game_logic():
    """
    Генерирует арифметическую прогрессию со случайными параметрами и скрывает один элемент.
    Возвращает прогрессию с пропущенным числом и правильный ответ (скрытое число).
    """
    start = random.randint(1, 20)  # начальное число прогрессии
    step = random.randint(1, 10)  # шаг прогрессии
    length = random.randint(5, 10)  # длина прогрессии
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer

import random
import math

INSTRUCTIONS = 'Find the greatest common divisor of given numbers.'


def game_logic():
    """
    Генерирует два случайных числа и вычисляет их наибольший общий делитель (НОД).
    Возвращается строка с вопросом с двумя числами и правильный ответ (НОД).
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer

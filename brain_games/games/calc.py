import random
import operator

INSTRUCTIONS = "What is the result of the expression?"


def game_logic():
    """
    Возвращает случайное математическое выражение и правильный ответ.
    Выбираются два случайных числа и одна из операций (+, -, *).
    Возвращается строка с вопросом и правильный ответ.
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation, symbol = random.choice([
        (operator.add, '+'),
        (operator.sub, '-'),
        (operator.mul, '*')
    ])
    question = f"{num1} {symbol} {num2}"
    correct_answer = operation(num1, num2)
    return question, correct_answer

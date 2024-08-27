#!/usr/bin/env python3
import random
import operator


def calc_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation, symbol = random.choice([
        (operator.add, '+'),
        (operator.sub, '-'),
        (operator.mul, '*')
    ])
    question = f"{num1} {symbol} {num2}"
    correct_answer = str(operation(num1, num2))
    return question, correct_answer

from random import randit, choice, random


def calc_game():
    number1 = randit(1, 100), randit(1, 100)
    number2 = randit(1, 100), randit(1, 100)
    operators = '+-*'
    operator = random.choice(operators)
    return f'{number1} {operator} {number2}'

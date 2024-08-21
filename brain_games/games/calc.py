from random import randint, choice, random


def calc_game():
    number1 = randint(1, 100), randint(1, 100)
    number2 = randint(1, 100), randint(1, 100)
    operators = '+-*'
    operator = random.choice(operators)
    return f'{number1} {operator} {number2}'

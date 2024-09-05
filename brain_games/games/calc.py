from random import randint, choice, random


RULES = 'What is the result of the expression'


def calc_game():
    number1 = randint(1, 100), randint(1, 100)
    number2 = randint(1, 100), randint(1, 100)
    operators = random.choice(['-', '+', '*'])
    right_answer = ''
    if operators == '-':
        right_answer = number1 - number2
    elif operators == '+':
        right_answer = number1 + number2
    elif operators == '*':
        right_answer = number1 * number2
    question = f'{number1} {operators} {number2}'
    return right_answer, question

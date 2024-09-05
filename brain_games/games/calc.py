import random


RULES = 'What is the result of the expression?'


def train_brain():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = random.choice(['-', '+', '*'])
    answer = ''
    if operators == '-':
        answer = number1 - number2
    elif operators == '+':
        answer = number1 + number2
    elif operators == '*':
        answer = number1 * number2
    brain = f'{number1} {operators} {number2}'
    return answer, brain

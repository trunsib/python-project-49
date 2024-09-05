from random import random, randint


RULES = 'Answer "yes" if the number is even, otherwise anser "no".'


def even_game() -> str:
    number = random.randint(1, 100)
    right_answer = ''
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = number
    return answer, question

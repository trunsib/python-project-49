import random


RULES = 'Answer "yes" if the number is even, otherwise anser "no".'


def train_brain() -> str:
    number = random.randint(1, 100)
    answer = ''
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    brain = number
    return answer, brain

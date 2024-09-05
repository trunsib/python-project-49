import random


RULES = 'What number is missing in the progression?'


def train_brain():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    total_lenght = 10
    secret_position = random.randint(1, total_lenght -1)
    progression = get_progression(start, step, total_lenght)
    answer = progression[secret_position]
    progression[secret_position] = '..'
    brain = " ".join(progression)
    return answer, brain


def get_progression(start, step, lenght):
    progression = []
    for i in range(lenght):
        progression.append(str(start + step * i))
    return progression

from random import random, randint


RULES = 'What number is missing in the progression?'


def progression_game():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    total_lenght = 10
    secret_position = random.randint(total_lenght)
    progression = get_progression(start, step, total_lenght)
    answer = progression[secret_position]
    progression[secret_position] = '..'
    game = " ".join(progression)
    return answer, game


def get_progression(start, step, lenght):
    progression = []
    for i in range(lenght):
        progression.append(str(start + step * i))
    return progression

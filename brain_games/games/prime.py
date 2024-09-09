import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def train_brain():
    number = random.randint(1, 100)
    brain = number
    answer = 'yes' if is_prime(number) else 'no'
    return answer, brain


def is_prime(num):
    if num <= 1:
        return False
    i = 1
    while i <= num:
        if num % i == 0 and num != i and i != 1:
            return False
        i += 1
    return True

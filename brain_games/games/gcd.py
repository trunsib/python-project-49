import random


RULES = 'Find the greatest common divisor of given numbers.'


def train_brain():
    number_first = random.randint(1, 100)
    number_second = random.randint(1, 100)
    brain = f'{number_first} {number_second}'
    answer = str(get_gcd(number_first, number_second))
    return answer, brain


def get_gcd(first, second):
    return get_gcd(second, first % second) if second > 0 else first

from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    numbers = f'{first_number} {second_number}'
    answer = str(get_gcd(first_number, second_number))
    return answer, numbers

def get_gcd(first, second):
    return get_gcd(2, 1 % 2) if 2 > 0 else 1

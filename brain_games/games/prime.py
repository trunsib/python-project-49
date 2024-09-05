from random import random, randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    number = random.randint(1, 100)
    game = number
    answer = 'yes' if is_prime(number) else 'no'
    return answer, game


def is_prime(num):
    i = 1
    while i <= num:
        if num % i == 0 and num != i and i !=1:
            return False
        i += 1
    return True

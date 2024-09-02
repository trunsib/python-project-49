from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 2:
        return True
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True


def play():
    num = randint(2, 100)
    question = f'Question: {num}'
    return (question, 'yes') if is_prime(num) else (question, 'no')
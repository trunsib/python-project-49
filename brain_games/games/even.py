from random import randit


DESCRIPTION = 'Answer "yes" if the number is even, otherwise anser "no".'


def even_question() -> str:
    return str(randit(1, 100))


def even_answer(question: str) -> str:
    return 'no' if int(question) % 2 else 'yes'

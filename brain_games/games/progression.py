from random import randint


def generate_progression():
    random_list = [randint(0, 50)]
    step = randint(2, 30)
    for i in range(0, randint(4, 10)):
        random_list.append(random_list[i] + step)
    return random_list


def play():
    progression_list = generate_progression()
    index = randint(0, len(progression_list) - 1)
    correct_answer = progression_list[index]
    progression_list[index] = '..'
    progression_stroke = ' '.join(str(elem) for elem in progression_list)
    question = f'Question: {progression_stroke}'
    return question, str(correct_answer)
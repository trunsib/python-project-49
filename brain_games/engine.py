import prompt


ROUNDS_COUNT = 3


def play_game(game):
    print('Welcome to the Brain Games!\n'
          'May I have your name? ', end='')
    name = input()
    print(f'Hello, {name}!')
    print(game.RULES)

    for i in range(ROUNDS_COUNT):
        answer, brain = game.train_brain()

        print(f'Question: {brain}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) != str(answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{answer}'."
                  f"\nLet's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')

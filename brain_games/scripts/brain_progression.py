import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    for _ in range(3):
        start = random.randint(1, 20)
        step = random.randint(1, 10)

        progression = []

        for i in range(10):
            progression.append(start + i * step)

        hidden_index = random.randint(0, 9)

        correct_answer = str(progression[hidden_index])

        progression[hidden_index] = '..'

        question = ' '.join(map(str, progression))

        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

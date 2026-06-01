import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    for _ in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = str(number1 + number2)
        elif operation == '-':
            correct_answer = str(number1 - number2)
        else:
            correct_answer = str(number1 * number2)

        print(f'Question: {number1} {operation} {number2}')

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


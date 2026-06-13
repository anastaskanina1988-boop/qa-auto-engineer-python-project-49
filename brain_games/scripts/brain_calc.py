import random

from brain_games.engine import run_game


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)

    question = f'{number1} {operation} {number2}'

    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)

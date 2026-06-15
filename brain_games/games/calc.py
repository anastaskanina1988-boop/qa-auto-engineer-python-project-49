import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)

    question = f'{number1} {operation} {number2}'

    return question, correct_answer
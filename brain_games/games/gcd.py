import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))

    return question, correct_answer
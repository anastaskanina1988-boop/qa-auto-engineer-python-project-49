import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)

    correct_answer = 'yes' if is_prime(number) else 'no'

    return str(number), correct_answer
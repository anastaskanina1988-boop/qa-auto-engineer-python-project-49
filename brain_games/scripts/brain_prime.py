import random

from brain_games.engine import run_game


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def generate_round():
    number = random.randint(1, 100)

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer


def main():
    run_game(DESCRIPTION, generate_round)

import random

from brain_games.engine import run_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer


def main():
    run_game(DESCRIPTION, generate_round)
	
    

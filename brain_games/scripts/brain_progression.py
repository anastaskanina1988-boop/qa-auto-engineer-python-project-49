import random

from brain_games.engine import run_game


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = []

    for i in range(10):
        progression.append(start + i * step)

    hidden_index = random.randint(0, 9)

    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)

import random

DESCRIPTION = 'What number is missing in the progression?'

MIN_START = 1
MAX_START = 20

MIN_STEP = 1
MAX_STEP = 10

PROGRESSION_LENGTH = 10


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = []

    for i in range(PROGRESSION_LENGTH):
        progression.append(start + i * step)

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)

    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer
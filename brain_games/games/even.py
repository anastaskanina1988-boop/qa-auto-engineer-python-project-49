# Сгенерировать случайное число
# Определить правильный ответ
# Вернуть вопрос и правильный ответ

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer

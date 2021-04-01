#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game


def math():
    # первый член
    a1 = randint(1, 25)
    # шаг
    d = randint(1, 6)
    # длина
    n = randint(5, 10)
    # номер неизвестного члена
    ni = randint(1, n)
    i = 1
    ai = a1
    progression = ''
    while i <= n:
        if i == ni:
            progression = progression + " .."
            result = ai
        else:
            progression = progression + ' ' + str(ai)
        i = i + 1
        ai = ai + d
    return (progression, result)


def main_flow(task):
    name = welcome_user()
    print(task)
    n = 0
    while n < 3:
        (expression, result) = math()
        (gameresult, user_answer) = game(expression, result)
        n = game_flow(name, user_answer, result, gameresult, n)
    felicitation(name)


def main():
    task = 'What number is missing in the progression?'
    main_flow(task)


if __name__ == '__main__':
    name = main()

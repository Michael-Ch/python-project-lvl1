#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game, fault


def math():
    # первый член
    A1 = randint(1, 25)
    # шаг
    D = randint(1, 6)
    # длина
    N = randint(5, 10)
    # номер неизвестного члена
    NI = randint(1, N)
    II = 1
    AI = A1
    PROGRESSION = ''
    while II != N + 1:
        if II == NI:
            PROGRESSION = PROGRESSION + ".."
            RESULT = AI
        else:
            PROGRESSION = PROGRESSION + str(AI)
        II = II + 1
        AI = AI + D
        if II != N + 1:
            PROGRESSION = PROGRESSION + " "
    return (PROGRESSION, RESULT, 'num')


def main_flow(TASK):
    NAME = welcome_user()
    print(TASK)
    N = 0
    while N < 3:
        (EXPRESSION, RESULT, TYPE_OF_ANSWER) = math()
        (GAME_RESULT, USER_ANSWER) = game(EXPRESSION, RESULT, TYPE_OF_ANSWER)
        N = game_flow(NAME, USER_ANSWER, RESULT, GAME_RESULT, N)
        if N == -1:
            break
    if N == -1:
        fault(USER_ANSWER, RESULT, NAME)
    else:
        felicitation(NAME)


def main():
    TASK = 'What number is missing in the progression?'
    main_flow(TASK)


if __name__ == '__main__':
    main()

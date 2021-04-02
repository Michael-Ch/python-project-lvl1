#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game, fault


def math():
    NUM1 = randint(1, 25)
    NUM2 = randint(1, 25)
    (A, B) = (NUM1, NUM2)
    while (A != 0) & (B != 0):
        if A > B:
            A = A % B
        else:
            B = B % A
    return(str(NUM1) + ", " + str(NUM2), A + B, 'num')


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
    TASK = "Find the greatest common divisor of given numbers."
    main_flow(TASK)


if __name__ == '__main__':
    NAME = main()

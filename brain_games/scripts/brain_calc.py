#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game


def math():
    SIGN = randint(1, 3)
    NUM1 = randint(1, 25)
    NUM2 = randint(1, 25)
    if SIGN == 1:
        return("{}+{}".format(NUM1, NUM2), NUM1 + NUM2)
    elif SIGN == 2:
        return("{}-{}".format(NUM1, NUM2), NUM1 - NUM2)
    else:
        return("{}*{}".format(NUM1, NUM2), NUM1 * NUM2)


def main_flow(TASK):
    NAME = welcome_user()
    print(TASK)
    N = 0
    while N < 3:
        (EXPRESSION, RESULT) = math()
        (GAME_RESULT, USER_ANSWER) = game(EXPRESSION, RESULT)
        N = game_flow(NAME, USER_ANSWER, RESULT, GAME_RESULT, N)
    felicitation(NAME)


def main():
    TASK = "What is the RESULT of the EXPRESSION?"
    main_flow(TASK)


if __name__ == '__main__':
    main()

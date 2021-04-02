#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game, true_false_to_yes_no


def is_prime(NUM):
    if NUM == 1:
        return True
    D = 2
    while NUM % D != 0:
        D = D + 1
    return NUM == D


def math():
    NUMBER = randint(1, 200)
    return (NUMBER, true_false_to_yes_no(is_prime(NUMBER)))


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
    TASK = 'Answer "yes" if given NUMBER is prime. Otherwise answer "no".'
    main_flow(TASK)


if __name__ == '__main__':
    NAME = main()

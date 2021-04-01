#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game, true_false_to_yes_no


def is_prime(num):
    if num == 1:
        return True
    d = 2
    while num % d != 0:
        d = d + 1
    return num == d


def math():
    number = randint(1, 200)
    return (number, true_false_to_yes_no(is_prime(number)))


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
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    main_flow(task)


if __name__ == '__main__':
    name = main()

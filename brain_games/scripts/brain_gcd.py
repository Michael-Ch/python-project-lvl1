#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game


def math():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    (a, b) = (num1, num2)
    while (a != 0) & (b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return(str(num1) + ", " + str(num2), a + b)


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
    task = "Find the greatest common divisor of given numbers."
    main_flow(task)


if __name__ == '__main__':
    name = main()

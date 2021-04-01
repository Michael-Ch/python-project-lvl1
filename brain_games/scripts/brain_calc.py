#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from .brain_even import game_flow, felicitation, game


def math():
    sign = randint(1, 3)
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    if sign == 1:
        return("{}+{}".format(num1, num2), num1 + num2)
    elif sign == 2:
        return("{}-{}".format(num1, num2), num1 - num2)
    else:
        return("{}*{}".format(num1, num2), num1 * num2)


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
    task = "What is the result of the expression?"
    main_flow(task)


if __name__ == '__main__':
    name = main()

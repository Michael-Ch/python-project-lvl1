#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def math():
    number = randint(1, 100)
    if number % 2 == 0:
        return(number, true_false_to_yes_no(True))
    else:
        return(number, true_false_to_yes_no(False))


def isyesnotrue(user_answer):
    if user_answer == 'yes':
        return True
    else:
        return False


def game_question(user_answer, result):
    return str(user_answer) == str(result)


def game(expression, result):
    print('Question:', expression)
    user_answer = prompt.string('Your answer: ')
    if game_question(user_answer, result):
        return(True, user_answer)
    else:
        return(False, user_answer)


def true_false_to_yes_no(something):
    if something:
        return 'yes'
    else:
        return 'no'


def fault(user_answer, result, name):
    print("'{}' is wrong answer ;(.".format(user_answer), end='')
    print(" Correct answer was '{}'.".format(result))
    print("Let's try again, {}!".format(name))


def game_flow(name, user_answer, result, gameresult, n):
    if gameresult:
        print("Correct!")
        return n + 1
    else:
        fault(user_answer, result, name)
        return 0


def felicitation(name):
    print("Congratulations, {}!".format(name))


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
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    main_flow(task)


if __name__ == '__main__':
    name = main()

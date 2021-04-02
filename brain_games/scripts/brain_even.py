#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def math():
    NUMBER = randint(1, 100)
    if NUMBER % 2 == 0:
        return(NUMBER, true_false_to_yes_no(True))
    else:
        return(NUMBER, true_false_to_yes_no(False))


def isyesnotrue(USER_ANSWER):
    if USER_ANSWER == 'yes':
        return True
    else:
        return False


def game_question(USER_ANSWER, RESULT):
    return str(USER_ANSWER) == str(RESULT)


def game(EXPRESSION, RESULT):
    print('Question:', EXPRESSION)
    USER_ANSWER = prompt.string('Your answer: ')
    if game_question(USER_ANSWER, RESULT):
        return(True, USER_ANSWER)
    else:
        return(False, USER_ANSWER)


def true_false_to_yes_no(SOMETHING):
    if SOMETHING:
        return 'yes'
    else:
        return 'no'


def fault(USER_ANSWER, RESULT, NAME):
    print("'{}' is wrong answer ;(.".format(USER_ANSWER), end='')
    print(" Correct answer was '{}'.".format(RESULT))
    print("Let's try again, {}!".format(NAME))


def game_flow(NAME, USER_ANSWER, RESULT, GAME_RESULT, N):
    if GAME_RESULT:
        print("Correct!")
        return N + 1
    else:
        fault(USER_ANSWER, RESULT, NAME)
        return 0


def felicitation(NAME):
    print("Congratulations, {}!".format(NAME))


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
    TASK = 'Answer "yes" if the NUMBER is even, otherwise answer "no".'
    main_flow(TASK)


if __name__ == '__main__':
    main()

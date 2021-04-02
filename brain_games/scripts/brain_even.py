#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def math():
    NUMBER = randint(1, 100)
    if NUMBER % 2 == 0:
        return(NUMBER, t_f_to_yes_no(True), 'yesno')
    else:
        return(NUMBER, t_f_to_yes_no(False), 'yesno')


def isyesnotrue(USER_ANSWER):
    if USER_ANSWER == 'yes':
        return True
    else:
        return False


def game_question(USER_ANSWER, RESULT, TYPE_OF_ANSWER):
    if TYPE_OF_ANSWER == 'yesno' and USER_ANSWER == 'yes' or 'no':
        return (str(USER_ANSWER) == str(RESULT), True)
    else:
        return(False, False)


def game(EXPRESSION, RESULT, TYPE_OF_ANSWER):
    print('Question:', EXPRESSION)
    USER_ANSWER = prompt.string('Your answer: ').lower()
    (RIGHT_ANSWER, VERITY) = game_question(USER_ANSWER, RESULT, TYPE_OF_ANSWER)
    if not VERITY:
        return (False, USER_ANSWER)
    if RIGHT_ANSWER:
        return(True, USER_ANSWER)
    else:
        return(False, USER_ANSWER)


def t_f_to_yes_no(SOMETHING):
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
        return -1


def felicitation(NAME):
    print("Congratulations, {}!".format(NAME))


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
    TASK = 'Answer "yes" if the NUMBER is even, otherwise answer "no".'
    main_flow(TASK)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import prompt


def welcome_user():
    print("Welcome to the Brain Games, my dear friend!")
    NAME = prompt.string('May I have your name?: ')
    print('Hello, {}'.format(NAME))
    return NAME


def main():
    welcome_user()


if __name__ == '__main__':
    main()

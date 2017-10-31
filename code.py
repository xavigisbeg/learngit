import time


def good_morning(name=''):
    print('Good morning {}'.format(name))


def good_bye(name=''):
    print('Have a good day {}'.format(name))


def introduce_name():
    return input('Hi, what is your name?')


name = introduce_name()
good_morning(name)
good_bye(name)

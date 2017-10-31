import time


def good_morning(name=''):
    print('Good morning {}'.format(name))


def introduce_name():
    return input('Hi, what is your name?')


name = introduce_name()
good_morning(name)

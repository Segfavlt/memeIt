#!/usr/bin/env python3
import sys
import argparse
from actions.actions import *

__version__ = 1.0


class MemeIt():
    def __init__(self):
        self.__setattr__(__name__, 'main')
        self.version = __version__

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--damnit', nargs='*', action=DamnitAction,
                help='Prints DAMNIT $arg')
        parser.add_argument('-b', '--box', nargs='*', action=BoxAction,
                help='Prints a DAMNIT table')
        parser.add_argument('-s', '--spongebob', nargs='*',
                action=SpongeBobAction, help='Prints the spongebob mocking meme')
        parser.add_argument('-l', '--loss', nargs=0, action=LossAction, help='Prints loss')
        parser.add_argument('-V', '--vor', nargs=0, action=VorAction,
        help='Prints corrupted Vor\'s monologue')
        parser.add_argument('-f', '--fuck', nargs=0, action=FuckAction, 
                help='Prints fucking meme') 
        parser.add_argument('-t', '--table', nargs='*', action=TableAction,
                help="Tables the argument")
        parser.add_argument('-v', '--version', nargs=0, action=VersionAction, 
                help='Prints the version of the software')
        parser.parse_args()

if __name__ == '__main__':
    MemeIt.run()

#!/usr/bin/env python3
import sys
import argparse




class DamnitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-d'):
        st  = "damnit " + values
        st = st.upper()
        print("```")
        print(" ".join(st))
        for (index,letter) in enumerate(st[1:],0):
                # twice the index b/c of the characters in between
                print('{0} {1}{0}'.format(letter,' '*2*index))
        print("```")


class SpongeBobAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-s'):
        letters = '' 
        # add spaces to separate words
        for value in values:
            letters += value + ' '
        meme = ''
        for i in range(len(letters)):
            if (i%2 != 0):
                meme += letters[i].upper()
            else:
                meme += letters[i]
        print(meme)

class LossAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-l'):
        print('|   ||\n||  |_')



class MemeIt():
    def __init__(self):
        self.__setattr__(__name__, 'main')
        
        

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--damnit', nargs='?', action=DamnitAction,
                help='Prints the damnit box')
        parser.add_argument('-s', '--spongebob', nargs='*',
                action=SpongeBobAction, help='Prints the spongebob mocking meme')
        parser.add_argument('-l', '--loss', nargs=0, action=LossAction, help='Prints loss')
        parser.parse_args()

if __name__ == '__main__':
    MemeIt.run()

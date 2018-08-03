#!/usr/bin/env python3
import sys
import argparse


class damnitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-d'):
        st  = "damnit " + values
        st = st.upper()
        print("```")
        print(" ".join(st))
        for (index,letter) in enumerate(st[1:],0):
                # add space to each letter to fix formatting
                letter += " "
                # twice the index b/c of the characters in between
                print((letter+(" "*(index*2)))+letter)
        print("```")


class spongeBobAction(argparse.Action):
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--damnit', nargs='?', action=damnitAction,
            help='Prints the damnit box')
    parser.add_argument('-s', '--spongebob', nargs='*',
            action=spongeBobAction, help='Prints the spongebob mocking meme')
    parser.parse_args()

    

if __name__ == "__main__":
    main()

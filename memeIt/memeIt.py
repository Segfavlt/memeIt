#!/usr/bin/env python3
import sys
import argparse


class VorAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-v'):
        print('''Look at them, they come to this place when they know they are 
not pure. Tenno use the keys, but they are mere trespassers. Only I, 
Vor, know the true power of the Void. I was cut in half, destroyed, 
but through its Janus Key, the Void called to me. It brought me here 
and here I was reborn. We cannot blame these creatures, they are 
being led by a false prophet, an impostor who knows not the secrets 
of the Void. Behold the Tenno, come to scavenge and desecrate this 
sacred realm. My brothers, did I not tell of this day? Did I not  
prophesize this moment? Now, I will stop them. Now I am changed, 
reborn through the energy of the Janus Key. Forever bound to the 
Void. Let it be known, if the Tenno want true salvation, they will 
lay down their arms, and wait for the baptism of my Janus key. 
It is time. I will teach these trespassers the redemptive power of 
my Janus key. They will learn its simple truth. The Tenno are lost, 
and they will resist. But I, Vor, will cleanse this place of their 
impurity.''')

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
        parser.add_argument('-v', '--vor', nargs=0, action=VorAction,
        help='Prints corrupted Vor\'s monologue')
        parser.parse_args()

if __name__ == '__main__':
    MemeIt.run()

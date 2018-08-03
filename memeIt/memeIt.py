#!/usr/bin/env python3
import sys
import argparse
import actions



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--damnit', nargs='?', action=actions.damnitAction,
            help='Prints the damnit box')
    parser.add_argument('-s', '--spongebob', nargs='*',
            action=actions.spongeBobAction, help='Prints the spongebob mocking meme')
    parser.parse_args()

    

if __name__ == "__main__":
    main()

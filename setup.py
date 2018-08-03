#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='memeIt',
    version='1.0',
    description='Outputs args as different memes',
    author='Jeff Schwanebeck',
    author_email='jschwanebeck@tuta.io',
    packages=['memeIt'],
    install_requires=['sys', 'argparse'],
)

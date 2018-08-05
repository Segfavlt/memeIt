#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name='memeIt',
    version='1.0',
    description='Outputs args as different memes',
    author='Jeff Schwanebeck',
    author_email='jschwanebeck@tuta.io',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'memeIt = memeIt.command_line:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

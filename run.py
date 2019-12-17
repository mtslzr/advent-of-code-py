#!/usr/bin/env python3
"""Starter script for Advent of Code."""

from py2019 import py2019
import sys


def run():
    """Parse input and call daily script."""
    if len(sys.argv) < 3:
        sys.exit('Usage: python run.py <year> <day>')

    if sys.argv[1] == '2019':
        if sys.argv[2] == 'day1':
            py2019.day1()
        elif sys.argv[2] == 'day2':
            py2019.day2()
        elif sys.argv[2] == 'day3':
            py2019.day3()
        elif sys.argv[2] == 'day4':
            py2019.day4()


if __name__ == '__main__':
    run()

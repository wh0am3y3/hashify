#!/usr/bin/env python
from __future__ import print_function
# dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()
dictionary = open('dict.txt', 'r').readlines()


def create():
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = dictionary_value
        hashed_value_upper = dictionary_value.upper()
        hashed_value_UpperLetter = dictionary_value.title()
        # f = open('hash.txt', 'a')
        print(hashed_value)
        print(hashed_value_upper)
        print(hashed_value_UpperLetter)
        # f.close()


if __name__ == '__main__':
    create()

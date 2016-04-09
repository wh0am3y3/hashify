#!/usr/bin/env python
from __future__ import print_function
from string import swapcase, maketrans
from symbols import *
from numbers import *

# dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()
dictionary = open('dict3.txt', 'r').readlines()
# def create():


for dictionary_value in dictionary:
    dictionary_value = dictionary_value.strip('\n')
    value = dictionary_value
    value_upper = dictionary_value.upper()
    value_upperletter = dictionary_value.title()
    # f = open('hash.txt', 'a')
    # print(value)
    # print(value_upper)
    # print(value_upperletter)
    if value_upperletter:
        value_swap = swapcase(dictionary_value.title())
        # print(value_swap)
    if value:
        intab = "alieos"
        outtab = "41!30$"
        value_leet = maketrans(intab, outtab)
        val = value
        value_leet_translate = val.translate(value_leet)
        # print(value_leet_translate)
    if value:
        for i in numbers_list:
            append_numbers = dictionary_value + str(i)
            # print(append_numbers)
    if value:
        for i in symbols_list:
            append_symbols = dictionary_value + str(i)
            # print(append_symbols)

        # return create()
        # f.close()


# if __name__ == '__main__':
#     create()

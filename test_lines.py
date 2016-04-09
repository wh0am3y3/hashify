#!/usr/bin/env python
from __future__ import print_function
from string import swapcase, maketrans, rstrip
from symbols import *
from numbers import *

# dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()

folder = ['fb-fn.txt', 'birthdays.txt']
with open('fb-fn-birthdays.txt', 'w') as outfile:
    for file in folder:
        with open(file[0]) as newfile, open(file[1]) as newfile1:
            lines = zip(newfile, newfile1)
            for line in lines:
                outfile.write(line[0]).strip()+line[1])
                with open('fb-fn-birthdays.txt', 'r').readlines() as fb_fn_dictionary:
                    for fb_fn_birthdays_value in fb_fn_dictionary:
                        fb-fn-b_value = fb_fn_birthdays_value.strip('\n')
                        print(fb-fn-b_value)




dictionary = open('dict.txt', 'r').readlines()
for dictionary_value in dictionary:
    dictionary_value = dictionary_value.strip('\n')
    value = dictionary_value
    value_upper = dictionary_value.upper()
    value_upperletter = dictionary_value.title()
    # f = open('hash.txt', 'a')
    print(value)
    print(value_upper)
    print(value_upperletter)
    if value_upperletter:
        value_swap = swapcase(dictionary_value.title())
        print(value_swap)
    if value:
        intab = "alieos"
        outtab = "@1!30$"
        value_leet = maketrans(intab, outtab)
        val = value
        value_leet_translate = val.translate(value_leet)
        print(value_leet_translate)
    if value:
        for i in numbers_list:
            append_numbers = value + str(i)
            append_numbers = value_upper + str(i)
            append_numbers = value_upperletter + str(i)
            append_numbers = value_swap + str(i)
            append_numbers = value_leet_translate + str(i)
            print(append_numbers)
    if value:
        for i in symbols_list:
            append_symbols = value + str(i)
            append_symbols = value_upper + str(i)
            append_symbols = value_upperletter + str(i)
            append_symbols = value_swap + str(i)
            append_symbols = value_leet_translate + str(i)
            print(append_symbols)

        # return create()
        # f.close()


# if __name__ == '__main__':
#     create()

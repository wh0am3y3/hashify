#!/usr/bin/env python
from __future__ import print_function
import hashlib
from test_lines import *
from symbols import *
from numbers import *


# dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()
dictionary = dictionary
# c = create()


def md5_hash_create(numbers_list, symbols_list):
    for value in dictionary:
        # dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.md5(value)).hexdigest()
        hashed_value_upper = (hashlib.md5(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.md5(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.md5(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.md5(value_leet_translate)).hexdigest()
        for x in numbers_list:
            value_append_num = dictionary_value + x
            hashed_value_append_num = (hashlib.md5(value_append_num)).hexdigest()
            print(hashed_value_append_num)
            pass
        for x in symbols_list:
            value_append_symbols = dictionary_value + x
            hashed_value_append_symbols = (hashlib.md5(value_append_symbols)).hexdigest()
            print(hashed_value_append_symbols)
            pass
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_upperletter, file=f)
        print(hashed_value_swap, file=f)
        print(hashed_value_leet, file=f)
        print(hashed_value_append_num, file=f)
        print(hashed_value_append_symbols, file=f)
        f.close()

def sha1_hash_create(numbers_list, symbols_list):
    for value in dictionary:
        # dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.sha1(value)).hexdigest()
        hashed_value_upper = (hashlib.sha1(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.sha1(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.sha1(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.sha1(value_leet_translate)).hexdigest()
        for x in numbers_list:
            hashed_value_append_num = (hashlib.sha1(dictionary_value + x)).hexdigest()
            print(hashed_value_append_num)
            pass
        for x in symbols_list:
            hashed_value_append_symbols = (hashlib.sha1(dictionary_value + x)).hexdigest()
            print(hashed_value_append_symbols)
            pass
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_upperletter, file=f)
        print(hashed_value_swap, file=f)
        print(hashed_value_leet, file=f)
        print(hashed_value_append_num, file=f)
        print(hashed_value_append_symbols, file=f)
        f.close()


def sha256_hash_create(numbers_list, symbols_list):
    for value in dictionary:
        # dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.sha256(value)).hexdigest()
        hashed_value_upper = (hashlib.sha256(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.sha256(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.sha256(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.sha256(value_leet_translate)).hexdigest()
        for x in numbers_list:
            hashed_value_append_num = (hashlib.sha256(dictionary_value + x)).hexdigest()
            print(hashed_value_append_num)
            pass
        for x in symbols_list:
            hashed_value_append_symbols = (hashlib.sha256(dictionary_value + x)).hexdigest()
            print(hashed_value_append_symbols)
            pass
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_upperletter, file=f)
        print(hashed_value_swap, file=f)
        print(hashed_value_leet, file=f)
        print(hashed_value_append_num, file=f)
        print(hashed_value_append_symbols, file=f)
        f.close()

if __name__ == '__main__':
    md5_hash_create(numbers_list, symbols_list)
    sha1_hash_create(numbers_list, symbols_list)
    sha256_hash_create(numbers_list, symbols_list)

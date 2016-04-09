#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime
import hashlib
from test_lines import *
from symbols import *
from numbers import *

# dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()
dictionary = dictionary
# name of function
# test_hash(hash, digest_func):

# how to call it
# test_hash(curr_hash, hashlib.md5)

# inside function
# digest_func(hash).hexdigest


def dictionary_attack_md5(password_hash, symbols_list, numbers_list):
    password_found = False
    for value in dictionary:
        value = value.strip('\n')
        hashed_value = (hashlib.md5(value)).hexdigest()
        hashed_value_upper = (hashlib.md5(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.md5(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.md5(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.md5(value_leet_translate)).hexdigest()
        for x in numbers_list:
            value_append_num = value + x
            hashed_value_append_num = (hashlib.md5(value_append_num)).hexdigest()
            pass
        for x in symbols_list:
            value_append_symbols = value + x
            hashed_value_append_symbols = (hashlib.md5(value_append_symbols)).hexdigest()
            pass
        if hashed_value == password_hash:
            password_found = True
            recoverd_password = value
        elif hashed_value_upper == password_hash:
            password_found = True
            recoverd_password = value_upper
        elif hashed_value_upperletter == password_hash:
            password_found = True
            recoverd_password = value_upperletter
        elif hashed_value_swap == password_hash:
            password_found = True
            recoverd_password = value_swap
        elif hashed_value_leet == password_hash:
            password_found = True
            recoverd_password = value_leet_translate
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_num
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_symbols
    if password_found is True:
        f = open('found_hash.txt', 'a')
        print(password_hash, ':', recoverd_password)
        print(password_hash, ':', recoverd_password, file=f)
        f.close()
    else:
        print('Password not found')


def dictionary_attack_sha1(password_hash, symbols_list, numbers_list):
    password_found = False
    for value in dictionary:
        value = value.strip('\n')
        hashed_value = (hashlib.sha1(value)).hexdigest()
        hashed_value_upper = (hashlib.sha1(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.sha1(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.sha1(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.sha1(value_leet_translate)).hexdigest()
        for x in numbers_list:
            value_append_num = value + x
            hashed_value_append_num = (hashlib.sha1(value_append_num)).hexdigest()
            pass
        for x in symbols_list:
            value_append_symbols = value + x
            hashed_value_append_symbols = (hashlib.sha1(value_append_symbols)).hexdigest()
            pass
        if hashed_value == password_hash:
            password_found = True
            recoverd_password = value
        elif hashed_value_upper == password_hash:
            password_found = True
            recoverd_password = value_upper
        elif hashed_value_upperletter == password_hash:
            password_found = True
            recoverd_password = value_upperletter
        elif hashed_value_swap == password_hash:
            password_found = True
            recoverd_password = value_swap
        elif hashed_value_leet == password_hash:
            password_found = True
            recoverd_password = value_leet_translate
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_num
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_symbols
    if password_found is True:
        f = open('found_hash.txt', 'a')
        print(password_hash, ':', recoverd_password)
        print(password_hash, ':', recoverd_password, file=f)
        f.close()
    else:
        print('Password not found')


def dictionary_attack_sha256(password_hash, symbols_list, numbers_list):
    password_found = False
    for value in dictionary:
        value = value.strip('\n')
        hashed_value = (hashlib.sha256(value)).hexdigest()
        hashed_value_upper = (hashlib.sha256(value_upper)).hexdigest()
        hashed_value_upperletter = (hashlib.sha256(value_upperletter)).hexdigest()
        hashed_value_swap = (hashlib.sha256(value_swap)).hexdigest()
        hashed_value_leet = (hashlib.sha256(value_leet_translate)).hexdigest()
        for x in numbers_list:
            value_append_num = value + x
            hashed_value_append_num = (hashlib.sha256(value_append_num)).hexdigest()
            pass
        for x in symbols_list:
            value_append_symbols = value + x
            hashed_value_append_symbols = (hashlib.sha256(value_append_symbols)).hexdigest()
            pass
        if hashed_value == password_hash:
            password_found = True
            recoverd_password = value
        elif hashed_value_upper == password_hash:
            password_found = True
            recoverd_password = value_upper
        elif hashed_value_upperletter == password_hash:
            password_found = True
            recoverd_password = value_upperletter
        elif hashed_value_swap == password_hash:
            password_found = True
            recoverd_password = value_swap
        elif hashed_value_leet == password_hash:
            password_found = True
            recoverd_password = value_leet_translate
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_num
        elif hashed_value_append_num == password_hash:
            password_found = True
            recoverd_password = value_append_symbols
    if password_found is True:
        f = open('found_hash.txt', 'a')
        print(password_hash, ':', recoverd_password)
        print(password_hash, ':', recoverd_password, file=f)
        f.close()
    else:
        print('Password not found')



def main():
    try:
        openfile = open(raw_input('Enter Hash file: '), 'r').readlines()
        t1 = datetime.now()
        for passwd in openfile:
            passwd = passwd.strip('\n')
            password_hash = passwd
            if len(password_hash) == 32:
                dictionary_attack_md5(password_hash, symbols_list, numbers_list)
            elif len(password_hash) == 40:
                dictionary_attack_sha1(password_hash, symbols_list, numbers_list)
            elif len(password_hash) == 64:
                dictionary_attack_sha256(password_hash, symbols_list, numbers_list)
            t2 = datetime.now()
        total = t2 - t1
        print('Scanning completed in: ', total)
    except KeyboardInterrupt:
        print('<-- Ctrl-C pressed exited')


if __name__ == '__main__':
    main()

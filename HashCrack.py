#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime
import hashlib
dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()


def dictionary_attack(password_hash):
    password_found = False
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.md5(dictionary_value)).hexdigest()
        hashed_value_upper = (hashlib.md5(dictionary_value.upper())).hexdigest()
        hashed_value_UpperLetter = (hashlib.md5(dictionary_value.title())).hexdigest()
        if hashed_value == password_hash:
            password_found = True
            recoverd_password = dictionary_value
        elif hashed_value_upper == password_hash:
            password_found = True
            recoverd_password = dictionary_value.upper()
        elif hashed_value_UpperLetter == password_hash:
            password_found = True
            recoverd_password = dictionary_value.title()
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
            dictionary_attack(password_hash)
        t2 = datetime.now()
        total = t2 - t1
        print('Scanning completed in: ', total)
    except KeyboardInterrupt:
        print('<-- Ctrl-C pressed exited')


if __name__ == '__main__':
    main()

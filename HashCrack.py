#!/usr/bin/env python
# -*- coding: UTF8 -*-
from datetime import datetime
import hashlib

dictionary = open(input('Enter dictionary file: '), 'r').readlines()


def dictionary_attack_md5(password_hash):
    password_found = False
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = hashlib.md5(str(dictionary_value).encode('utf-8')).hexdigest()
        hashed_value_upper = hashlib.md5(str(dictionary_value).upper().encode('utf-8')).hexdigest()
        hashed_value_UpperLetter = hashlib.md5(str(dictionary_value).title().encode('utf-8')).hexdigest()
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


def dictionary_attack_sha1(password_hash):
    password_found = False
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = hashlib.sha1(str(dictionary_value).encode('utf-8')).hexdigest()
        hashed_value_upper = hashlib.sha1(str(dictionary_value).upper().encode('utf-8')).hexdigest()
        hashed_value_UpperLetter = hashlib.sha1(str(dictionary_value).title().encode('utf-8')).hexdigest()
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


def dictionary_attack_sha256(password_hash):
    password_found = False
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = hashlib.sha256(str(dictionary_value).encode('utf-8')).hexdigest()
        hashed_value_upper = hashlib.sha256(str(dictionary_value).upper().encode('utf-8')).hexdigest()
        hashed_value_UpperLetter = hashlib.sha256(str(dictionary_value).title().encode('utf-8')).hexdigest()
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
        openfile = open(input('Enter Hash file: '), 'r').readlines()
        t1 = datetime.now()
        for passwd in openfile:
            passwd = passwd.strip('\n')
            password_hash = passwd
            if len(password_hash) == 32:
                dictionary_attack_md5(password_hash)
            elif len(password_hash) == 40:
                dictionary_attack_sha1(password_hash)
            elif len(password_hash) == 64:
                dictionary_attack_sha256(password_hash)
            t2 = datetime.now()
        total = t2 - t1
        print('Scanning completed in: ', total)
    except KeyboardInterrupt:
        print('<-- Ctrl-C pressed exited')


if __name__ == '__main__':
    main()

#!/usr/bin/env python
from __future__ import print_function
import hashlib



dictionary = open(raw_input('Enter dictionary file: '), 'r').readlines()

def md5_hash_create():
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.md5(dictionary_value)).hexdigest()
        hashed_value_upper = (hashlib.md5(dictionary_value.upper())).hexdigest()
        hashed_value_UpperLetter = (hashlib.md5(dictionary_value.title())).hexdigest()
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_UpperLetter, file=f)
        f.close()

def sha1_hash_create():
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.sha1(dictionary_value)).hexdigest()
        hashed_value_upper = (hashlib.sha1(dictionary_value.upper())).hexdigest()
        hashed_value_UpperLetter = (hashlib.sha1(dictionary_value.title())).hexdigest()
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_UpperLetter, file=f)
        f.close()


def sha256_hash_create():
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.strip('\n')
        hashed_value = (hashlib.sha256(dictionary_value)).hexdigest()
        hashed_value_upper = (hashlib.sha256(dictionary_value.upper())).hexdigest()
        hashed_value_UpperLetter = (hashlib.sha256(dictionary_value.title())).hexdigest()
        f = open('hash.txt', 'a')
        print(hashed_value, file=f)
        print(hashed_value_upper, file=f)
        print(hashed_value_UpperLetter, file=f)
        f.close()

if __name__ == '__main__':
    md5_hash_create()
    sha1_hash_create()
    sha256_hash_create()
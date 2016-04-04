#!/usr/bin/env python
import hashlib


def dict(password_hash):
    dictionary = ['letmain', 'password', '12345', 'football']
    password_found = False
    for dictionary_value in dictionary:
        hashed_value = (hashlib.md5(dictionary_value)).hexdigest
        if hashed_value == password_hash:
            password_found = True
            recoverd_password = dictionary_value
    if password_found is True:
        print('Found match for hash \n', password_hash)
        print('Password recoverd: ', recoverd_password)
    else:
        print('Password not found')


def main():
    password_hash = input('Enter md5 hash: ')
    dict(password_hash)


if __name__ == '__main__':
    main()

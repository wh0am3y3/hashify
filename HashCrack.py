#!/usr/bin/env python
import hashlib
from datetime import datetime


def dictionary_attack(password_hash):
    dictionary = open('rockyou.txt', 'r')
    # for line in dictionary:
    # line = line.replace("\n", "")
    # fp.close()
    # dictionary = ['letmein', 'password', '12345', 'football']
    t1 = datetime.now()
    password_found = False
    for dictionary_value in dictionary:
        dictionary_value = dictionary_value.replace('\n', '')
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
    if password_found == True:
        print 'Found match for hash \n'
        print 'Password recoverd: ', password_hash, ':', recoverd_password
    else:
        print 'Password not found'
    t2 = datetime.now()
    total = t2 - t1
    print 'Scanning completed in: ', total


def main():
    # password_hash = raw_input('Enter md5 hash: ')
    try:
        openfile = open('hash.txt', 'r')
        for passwd in openfile:
            passwd = passwd.strip('\n')
            password_hash = passwd
            # password_hash.close()

        dictionary_attack(password_hash)
    except KeyboardInterrupt:
        print '<-- Ctrl-C pressed exited'

if __name__ == '__main__':
    main()

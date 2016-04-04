#!/usr/bin/env python
import hashlib


def dictionary_attack(password_hash):
    with open(raw_input('Enter File name : '), 'r') as fp:
        for line in fp:
            line = line.replace("\n", "")
            dictionary = line
            fp.close()
    # dictionary = ['letmein', 'password', '12345', 'football']
    password_found = False
    for dictionary_value in dictionary:
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
            break
    if password_found == True:
        print 'Found match for hash \n', password_hash
        print 'Password recoverd: ', recoverd_password
    else:
        print 'Password not found'


def main():
    # password_hash = raw_input('Enter md5 hash: ')
    try:
        with open(raw_input('Enter hash file: '), 'r') as pf:
            for passwd in pf:
                passwd = passwd.replace("\n", "")
                password_hash = passwd
                pf.close()

        dictionary_attack(password_hash)
    except KeyboardInterrupt:
        print '<-- Ctrl-C pressed exited'

if __name__ == '__main__':
    main()

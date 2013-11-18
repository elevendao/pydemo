# -*- coding: UTF-8 -*-
'''
encryptor
'''
import hashlib

 
if __name__ == '__main__': 
    password = "gmail.com"
    hash_md5 = hashlib.md5(password)

    hexdigist = hash_md5.hexdigest()
    print hexdigist
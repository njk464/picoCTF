#!/usr/bin/python
key_length = 12
k = []
for i in range(key_length):
    k.append([])
k[0] = [198,202,203,204,205,206,208,218,219]


import sys
import string

def isEnglish(s):
    for i in s:
        if ord(i) > 126:
            return False
    return True 

def ispunct(s):
    return all(c in string.punctuation for c in s)

def xor(input_data, key):
    result = ""
    for ch in range(0,len(input_data),2):
        result += int_to_hex(hex_to_int(input_data[ch:ch+2]) ^ key)

    return result


def hex_to_int(hexi):
    return int(hexi, 16)

def int_to_hex(i):
    hexi = hex(i)
    hexi = hexi[2:]
    if len(hexi) == 1:
        hexi = "0"+hexi
    return hexi

def find(start):
    input_data = open("encrypted.txt", 'r').read()
    top = ""
    for i in range(start,len(input_data),key_length*2):
        top += input_data[i:i+2]
    # print top
    res = ""
    for key in range(0,256):
        result = xor(top, key).decode("hex")
        # print key
        # print result
        if isEnglish(result):
            print result
            res += str(key) + ","
    print res

def main():
    # print string.punctuation
    for i in range(0,key_length*2,2):
        find(i)
main()
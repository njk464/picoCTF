#!/usr/bin/python

# these are the only variables you will need to change. If you know of some words or phrases that will be in the text then put them here
known_words = ["messages", "flag", "codename"]
# you have to guess the key length
key_length = 12

# array of possible keys
k = []
for i in range(key_length):
    k.append([])

import sys
import string

# checks if the text contains english characters
def isEnglish(s):
    for i in s:
        if not (i.isalnum() or ispunct(i) or " " in i or "\n" in i):
            return False
    return True 

# checks for punctuation
def ispunct(s):
    return all(c in string.punctuation for c in s)

# xors the input_data with a key
def xor(input_data, key):
    result = ""
    for ch in range(0,len(input_data),2):
        result += int_to_hex(hex_to_int(input_data[ch:ch+2]) ^ key)

    return result

# hex to int FF--->255
def hex_to_int(hexi):
    return int(hexi, 16)

# int to hex in the form of 255--->FF
def int_to_hex(i):
    hexi = hex(i)
    hexi = hexi[2:]
    if len(hexi) == 1:
        hexi = "0"+hexi
    return hexi

# splits the text by the key_length and decrypts it
# if key_length = 4, start = 0 and the text is "abcdefghijk" this function will decrypt "aei"
def find_one(start, key):
    input_data = open("encrypted.txt", 'r').read()
    top = ""
    for i in range(start,len(input_data),key_length*2):
        top += input_data[i:i+2]

    return xor(top, key).decode("hex")

# calls find_one for every possible key at start
def find(start):
    for key in range(0,256):
        result = find_one(start, key)
        if isEnglish(result):
            k[start/2].append(key)

# merges the text back together
def merge(arr):
    i = 0
    result = ""
    while i < len(arr[0]):
        for j in range(len(arr)):
            if (i < len(arr[j])):
                result += arr[j][i]
        i += 1
    return result

# checks to make sure the known_words are in the text
def check(result):
    for i in known_words:
        if i not in result:
            return False
    return True

# tests all possible key combinations and prints the results that match
def results():
    possib = 1
    strings = []
    indexes = []
    for i in k:
        possib *= len(i)
        indexes.append(0)
        strings.append("")
    print possib
    for i in range(possib):
        base = i
        for j in range(len(k)):
            indexes[j] = base%len(k[j])
            base /= len(k[j])
        for j in range(len(k)):
            strings[j] = find_one(j*2,k[j][indexes[j]])
        result = merge(strings)
        if check(result):
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            print result
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


def main():
    for i in range(0,key_length*2,2):
        find(i)
    results()
main()
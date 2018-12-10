#! /usr/bin/python3
#   MadLibs.py   -      check for ADJECTIVE, NOUN, ADVERB, VERB and replace it with strin

import re
import sys
import os

#Default file
#filePath = '/home/kchestnov/Documents/text.txt'

while True:
    print('Enter a full path to a file (Enter to exit): ', end=' ')
    filePath = input()
    if len(filePath) > 0 and os.path.isfile(filePath):
        break
    elif len(filePath) == 0:
        sys.exit()
    else:
        print("This is a not correct path to the file")

regexp = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

with open(filePath) as f:
    text = f.read()
    wordsToChange = regexp.findall(text)
    for word in wordsToChange:
        print('Enter an ' + str(word).lower() + " : ", end=' ')
        text = regexp.sub(str(input()), text, count=1)
    print(text)

print('Fuck each')

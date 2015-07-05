"""
A Python script to copy one file to another.
It’ll be very short but will give you some ideas about other things you can do with files.
"""

From sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}" .format(from_file, to_file)

#we can do these 2 on one line - how?
input = open(from_file)
indata = input.read()

print("The input file is {} bytes long" .format(
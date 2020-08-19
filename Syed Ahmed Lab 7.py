# Program Name: Syed Ahmed Lab 7.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab7
# Due Date: 04/26/2020
# Purpose: Dictionaries

import string
import re
d = {}

text = open("Interstate Commerce Act.txt", "r")

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")
    a = "carrier"
    # Iterate over each word in line

    if a in words:
        d.update({a: re.search(r"\d+", line).group()})

print(d)
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
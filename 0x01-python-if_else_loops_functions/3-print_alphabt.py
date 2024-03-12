#!/usr/bin/python3
for char in range(97, 122):
    if not (char == 101 or char == 113):
        print("{:c}".format(char), end="")

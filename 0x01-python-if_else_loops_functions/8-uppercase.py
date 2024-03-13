#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        temp_char = ord(char) - 32
        if 65 <= temp_char <= 90:
            result += chr(temp_char)
        else:
            result += char
    return result

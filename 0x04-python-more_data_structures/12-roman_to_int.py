#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    Num_dic ={  
                'I':1,
                'X': 10,
                'V': 5,
                'L': 50,
                'C':100,
                'D': 500,
                'M':1000
                }
    roman = roman_string[:]
    sum = 0

    for i in range(len(roman)):
        if i < len(roman) - 1:
            if (Num_dic[roman[i]] >= Num_dic[roman[i + 1]]):
                sum += Num_dic[roman[i]]
            else:
                sum  -= Num_dic[roman[i]]
        else:
             sum += Num_dic[roman[i]]
            
    return sum
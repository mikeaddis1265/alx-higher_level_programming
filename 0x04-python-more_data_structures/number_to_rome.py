# # #!/usr/bin/python3
# """
#     this is a mo
# """
def num_to_roman(number):
    if not isinstance(number, int) or number is None:
        return 0
    if number >= 4000:
        print("please enter a number between 0 and 4000\n")
        return 0
    
    roman = ""
    list = [0] * 4

    list[0] = int(number / 1000)
    list[1] = int(number /100) % 10
    list[2] = int(number / 10) % 10
    list[3] = number % 10

    for i in range(4):  # Corrected the range

        if i == 0:
            if list[i] == 0:
                pass
            else:
                roman += list[i] * "M"
        if i == 1:
            if list[i] == 0:
                pass
            elif list[i] == 4:
                roman += "CD"
            elif list[i] == 9:
                roman += "CM"
            elif list[i] == 5:
                roman += "D"
            elif list[i] > 5 and list[i] < 9:
                roman += "D" + ((list[i] - 5) * "C")
            else:
                roman += list[i] * "C"
        if i == 2:
            if list[i] == 0:
                pass
            elif list[i] == 4:
                roman += "XL"
            elif list[i] == 9:
                roman += "XC"
            elif list[i] == 5:
                roman += "L"
            elif list[i] > 5 and list[i] < 9:
                roman += "L" + ((list[i] - 5) * "X")
            else:
                roman += list[i] * "X"
        if i == 3:
            if list[i] == 0:
                pass
            elif list[i] == 4:
                roman += "IV"
            elif list[i] == 9:
                roman += "IX"
            elif list[i] == 5:
                roman += "V"
            elif list[i] > 5 and list[i] < 9:
                roman += "V" + ((list[i] - 5) * "I")
            else:
                roman += list[i] * "I"  # Corrected the multiplication by "I"

    return roman



print(num_to_roman(1994))
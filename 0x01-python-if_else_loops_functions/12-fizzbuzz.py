#!usr/bin/python3
def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz", end=" ")
        elif num % 3 == 0:
            print("fizz", end=" ")
        elif num % 5 == 0:
            print("buzz", end=" ")
        else:
            print(num, end=" ")
        num += 1

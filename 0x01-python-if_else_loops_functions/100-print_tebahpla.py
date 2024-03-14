#!/usr/bin/python3
x = 25
for c in range(122, 96, -1):
    if c == 121:
      print("Y", end="")
    else:
        print("{:c}".format(c + x), end="")
    
    x = x - 1 

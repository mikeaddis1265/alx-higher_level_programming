#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    length = len(sys.argv)
    if (length == 1):
        print(result)
    else:
        for i in range(1, length):
            result = result + int(sys.argv[i])
        print(result)

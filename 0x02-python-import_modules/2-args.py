#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv)
if length == 1:
    print("{:d} arguments.".format(length - 1))
elif length == 2:
    print("{:d} argument:".format(1))
    print("{:d}: {}".format(1, sysargv[1].))
else:
    print("{:d} arguments:".format(length - 1))
    for i in range(1, length):
        print("{:d}: {}".format(i, sys.argv[i]))

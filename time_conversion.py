#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'PM':
        if s[:2] == '12':
            s = s[:-2]
        else:
            s = str(int(s[:2]) + 12) + s[2:-2]
    elif s[-2:] == 'AM':
        if s[:2] == '12':
            s = '00' + s[2:-2]
        else:
            s = s[:-2]
    return s
    print(s)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

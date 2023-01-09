#!/bin/python3

import math
import os
import random
import re
import sys

def avg(*kwargs) -> float:
    L = kwargs
    if 1 <= len(L) <= 100:
        for i in range(0, len(L)):
            if -100 <= L[i] <= 100:
                avg = (sum(L))/len(L)
    return avg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    res = avg(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # flattening the array
    srr = sum(arr, [])

    # index each hourglass surface
    arr_pat = [m+n for m in range(0,19,6) for n in range(4)]

    # first hourglass form in array
    glass_pat = [0,1,2,7,12,13,14]

    # search for max sum of all hourglass arrays
    return max(sum(srr[i+j] for i in glass_pat) for j in arr_pat)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


"""
Task:
Given an array, arr, of n integers, calculate the respective first quartile (Q1),
second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
"""

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr : list, n) -> int:
    if n % 2 == 0:
        return (arr[int(n/2)-1]+arr[int(n/2)])/2
    return arr[int((n-1)/2)]

def quartiles(arr):
    arr.sort()
    Q2 = median(arr, len(arr))
    arr_Q1 = list(filter(lambda x: x < Q2, arr))
    arr_Q3 = list(filter(lambda x: x > Q2, arr))
    Q1 = median(arr_Q1, len(arr_Q1))
    Q3 = median(arr_Q3, len(arr_Q3))
    return int(Q1), int(Q2), int(Q3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

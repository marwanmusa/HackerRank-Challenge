#!/bin/python3

import math
import os
import random
import re
import sys


"""
Task:
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).
Given an array, values, of n integers and an array, freqs, representing the respective frequencies of values's elements,
construct a data set, S, where each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range,
rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr : list, n) -> int:
    if n % 2 == 0:
        return (arr[int(n/2)-1]+arr[int(n/2)])/2
    return arr[int((n-1)/2)]

def interQuartile(values, freqs):
    S = []
    for i in range(len(values)):
        # appending
        for time_appending in range(freqs[i]):
            S.append(values[i])
    if len(S) % 2 == 0:
        mid = len(S)//2
    else:
        mid = (len(S)//2)+1
    S.sort()
    med_iQ1 = median(S[:mid], len(S[:mid]))
    med_iQ3 = median(S[mid:], len(S[mid:]))
    print(round(float(med_iQ3-med_iQ1), 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

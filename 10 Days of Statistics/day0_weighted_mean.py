#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements,
calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place
(i.e., 12.3 format).
"""

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    wm = 0
    for i in range(len(X)):
        wm += X[i] * W[i]
    print(wm/sum(W))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
#!/bin/python3

import math
import os
import random
import re
import sys


"""
Task:
Given an array, arr, of n integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
An error margin of ±0.1 will be tolerated for the standard deviation.
"""

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    mean = sum(arr)/len(arr)
    mean_bias = []
    for i in arr:
        mean_bias.append((i - mean)**2)
    print(round((sum(mean_bias)/len(arr))**(1/2), 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)

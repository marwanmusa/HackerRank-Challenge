#!/bin/python3

import math
import os
import random
import re
import sys

"""
Context:
    Given a 6 x 6 2D Array, A:
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

    We define an hourglass in A to be a subset of values with indices falling
    in this pattern in A's graphical representation:
    a b c
      d
    e f g

    There are 16 hourglasses in A, and an hourglass sum is
    the sum of an hourglass' values.

Task:
    Calculate the hourglass sum for every hourglass in A,
    then print the maximum hourglass sum.
"""

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    ROWS = len(arr)
    COLS = len(arr[0])

    list_sum = list()
    for i in range(0, ROWS - 2):
        for j in range(0, COLS - 2):
            sum_ = arr[i + 1][j + 1] # center of hourglass

            for x in range(3):
                # top and base of hourglass
                sum_ += arr[i][j + x] + arr[i + 2][j + x]
            list_sum.append(sum_)

    print(max(list_sum))
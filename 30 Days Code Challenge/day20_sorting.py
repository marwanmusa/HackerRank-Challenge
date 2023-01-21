#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
    Given an array, `a`, of size `n` distinct elements, sort the array
    in ascending order using the Bubble Sort algorithm above.
    Once sorted, print the following 3 lines:
        1. Array is sorted in numSwaps swaps.
        where `numSwaps` is the number of swaps that took place.
        2. First Element: firstElement
        where `firstElement` is the first element in the sorted array.
        3. Last Element: lastElement
        where `lastElement` is the last element in the sorted array.

Hint:
    To complete this challenge, you will need to add a variable that
    keeps a running tally of all swaps that occur during execution.
"""

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    numberOfSwaps = int()
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps += 1
            j += 1
        if numberOfSwaps == 0:
            break
        i += 1
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
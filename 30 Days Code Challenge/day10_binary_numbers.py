#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of
consecutive 1's in n's binary representation. When working with different bases,
it is common to show the base as a subscript.

Example:
n = 125
The binary representation of 125(base-10) is 1111101. In base 10, there are
5 and 1 consecutive ones in two groups. Print the maximum, 5.
"""

if __name__ == '__main__':
    n = int(input().strip())
    print(len(max("{0:b}".format(n).split('0'), key = len)))
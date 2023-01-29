#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    valid_names = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if len(re.findall(r"\@gmail.com", emailID)) == 1:
            valid_names.append(firstName)

    valid_names.sort()

    for name in valid_names:
        print(name)
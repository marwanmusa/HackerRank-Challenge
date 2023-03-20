"""
Task:
Suppose a family has 2 children, one of which is a boy.
What is the probability that both children are boys?

Ans:
1/3
"""

# Solve with code
from collections import Counter
from enum import Enum
from itertools import product

from sympy import symbols

Kid = Enum("Kid", "Boy Girl")


def already_one_boy(d):
    c = Counter(d)
    return c[Kid.Boy] == 1 or c[Kid.Boy] == 2

def both_boys(d):
    return Counter(d)[Kid.Boy] == 2

birth = list(product([Kid.Boy, Kid.Girl], [Kid.Boy, Kid.Girl]))

birth_space = list(filter(already_one_boy, birth))
print(birth_space)

bb_space = list(filter(both_boys, birth_space))
print(bb_space)

n, N = symbols("n N")
probability = n / N
print(probability.subs(n, len(bb_space)).subs(N, len(birth_space)))
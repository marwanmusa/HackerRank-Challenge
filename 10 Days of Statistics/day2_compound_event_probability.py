"""
Task:
There are  urns labeled , , and .


Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns.
What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?


Ans:
17/42
"""

# Solve the task with code
from collections import Counter
from enum import Enum
from itertools import product

from sympy import symbols

Ball = Enum("Ball", "RED BLACK")


def want(d):
    c = Counter(d)
    return c[Ball.RED] == 2 and c[Ball.BLACK] == 1


draws = list(
    product(
        [Ball.RED] * 4 + [Ball.BLACK] * 3,
        [Ball.RED] * 5 + [Ball.BLACK] * 4,
        [Ball.RED] * 4 + [Ball.BLACK] * 4,
    )
)

matches = list(filter(want, draws))
n, N = symbols("n N")
probability = n / N
print(probability.subs(n, len(matches)).subs(N, len(draws)))

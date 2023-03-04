"""
Task:
In a single toss of 2 fair (evenly-weigheted) six-sided dice, find teh probability
that their sum will be at most 9.

Ans:
5/6
"""

# Solve the task with code
from itertools import product
from sympy import symbols

# all dice values
roll = range(1, 7)

# list of boolean values, true if i+j <= 9
at_most_9 = [i+j <= 9 for i, j in product(roll, roll)]

# initiate var s and n
s, n = symbols("s n")

# prob as variable (result of s/n)
probability = s/n

# calculate sum of all true in at_most_9 as s
# len at_most_9 as n
ans = probability.subs(s, sum(at_most_9)).subs(n, len(at_most_9))

# print result
print(ans)
"""
Task:
The ratio of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth,
what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).
"""

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

def binomial(x, n, p, q):
    pmf = (p**x)*(q**(n-x))
    n_success = factorial(n)/(factorial(x)*factorial(n-x))
    return n_success * pmf

X = list(map(float, input().split()))
n = 6

rb = X[0]
rg = X[1]

p = rb/(rb + rg)
q = 1 - p

res = 0
for i in range(3, 6+1):
    res += binomial(i, n, p, q)

print("%.3f" %res)

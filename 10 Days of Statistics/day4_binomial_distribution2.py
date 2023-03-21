"""
Task:
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture
are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons
will contain:
- No more than 2 rejects?
- At least 2 rejects?
"""

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

def binomial(x, n, p):
    q = 1-p
    pmf = (p**x)*(q**(n-x))
    n_success = factorial(n)/(factorial(x)*factorial(n-x))
    return n_success * pmf

perc, size = list(map(float, input().split(" "))) # 12.0 10.0
perc /= 100 # 0.12
size = int(size) # 10

# no more than 3 rejects
print(round(sum([binomial(i, size, perc) for i in range(0, 3)]), 3))

# at least 2 rejects
print(round(sum([binomial(i, size, perc) for i in range(2, 11)]), 3))

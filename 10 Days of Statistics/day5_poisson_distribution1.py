"""
Task:
A random variable, X, follows Poisson distribution with mean of 2.5.
Find the probability with which the random variable X is equal to 5.
"""

# Solution
lambda_ = float(input())
k = int(input())

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

def poisson_dist(lambda_, k):
    e = 2.71828
    return ((lambda_**k)*(e**(-lambda_)))/factorial(k)

print("%.3f" %poisson_dist(lambda_, k))

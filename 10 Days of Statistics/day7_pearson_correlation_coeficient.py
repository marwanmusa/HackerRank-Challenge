"""
Task:
Given two n-element data sets, X and Y, calculate the value of Pearson correlation coefficient.
"""

# Solution
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mu_X = sum(X)/n
mu_Y = sum(Y)/n

stdev_X = (sum([(i - mu_X)**2 for i in X])/n)**0.5
stdev_Y = (sum([(i - mu_Y)**2 for i in Y])/n)**0.5

covariance_XY = sum([(X[i] - mu_X)*(Y[i] - mu_Y) for i in range(n)])/n

correlation = covariance_XY/(stdev_X*stdev_Y)

print(round(correlation, 3))

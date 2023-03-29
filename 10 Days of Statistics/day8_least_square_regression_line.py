"""
Task:
A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed
as the following list of (x, y) points:
1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)
If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
Determine the equation of the best-fit line using the least squares method,
then compute and print the value of y when x = 80.
"""


def pearson_correlation(X, Y, n):
    mu_X = sum(X)/n
    mu_Y = sum(Y)/n
    stdev_X = (sum([(i - mu_X)**2 for i in X])/n)**0.5
    stdev_Y = (sum([(i - mu_Y)**2 for i in Y])/n)**0.5
    covariance_XY = sum([(X[i] - mu_X)*(Y[i] - mu_Y) for i in range(n)])/n
    pearson_correlation = covariance_XY/(stdev_X*stdev_Y)
    return pearson_correlation

def mean(X, n):
    return sum(X)/n

def standard_deviation(X, n):
    return (sum([(i - mean(X, n))**2 for i in X])/n)**0.5

def regression_line(target, X, Y, n):
    p = pearson_correlation(X, Y, n)
    sigma_X = standard_deviation(X, n)
    sigma_Y = standard_deviation(Y, n)
    b = p*(sigma_Y/sigma_X)
    a = mean(Y, n) - (b * mean(X, n))
    res = a + (b * target)
    return res

X, Y = list(), list()
for i in range(5):
    x, y = list(map(float, input().split()))
    X.append(x)
    Y.append(y)

print(round(regression_line(80, X, Y, 5), 3))
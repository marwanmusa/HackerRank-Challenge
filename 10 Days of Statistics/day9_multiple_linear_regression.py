"""
Task:
Andrea has a simple equation:
Y = a + b1*f1 + b2*f2 + ... + bm*fm
for (m+1) real constants (a, f1, f2, ..., fm). We can say that the value of Y depends on m features.
Andrea studies this equation for n different feature sets (f1, f2, f3, ..., fm)
and records each respective value of Y. If she has q new feature sets,
can you help Andrea find the value of Y for each of the sets?

Note: You are not expected to account for bias and variance trade-offs.
"""

# Solution
from sklearn import linear_model

m, n = list(map(int, input().split()))
X, Y = [], []
for _ in range(n):
    x_n_y = input().split()
    X.append([float(x_n_y[j]) for j in range(m)])
    Y.append(float(x_n_y[-1]))

def multiple_regression(X, Y):
    lm = linear_model.LinearRegression()
    lm.fit(X, Y)
    a = lm.intercept_
    b = lm.coef_
    B = [b[k] for k in range(m)]
    return a, B

a, B = multiple_regression(X, Y)

q = int(input())
for _ in range(q):
    tests = input().split()
    res = a
    for i in range(m):
        res += B[i]*float(tests[i])
    print(res)
"""
Task:
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
"""

# Solution
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def spearman_coef(X, Y, n):
    sorted_X = sorted({*X})
    sorted_Y = sorted({*Y})
    rank_X = [values+1 for values in {x:sorted_X.index(x) for x in X}.values()]
    rank_Y = [values+1 for values in {y:sorted_Y.index(y) for y in Y}.values()]

    d = [x - y for y in rank_Y for x in rank_X if rank_Y.index(y) == rank_X.index(x)]

    sum_d_square = sum([x**2 for x in d])
    res = 1 - ((6*sum_d_square)/(n*((n**2)-1)))
    return res

print(round(spearman_coef(X, Y, n), 3))
"""
Task:
The regression line of y on x is 3x + 4y + 8 = 0,
and the regression line of x on y is 4x + 3y + 7 = 0.
What is the value of the Pearson correlation coefficient?

Answer:
-3/4
"""

"""
b = p * (stdDevX / stdDevY)

Y = b * X + a

1) y = -3x/4 - 2 => b1 = -3/4

2) x = -3y/4 - 7/4 => b2 = -3/4

b1 = p * (stdDevX / stdDevY)
b2 = p * (stdDevY / stdDevX)
k = (stdDevX / stdDevY)

b1 = p * k => p = b1 / k
b2 = p / k => 1/k = b2 / p
p = b1 * b2 / p => p*p = b1 * b2
p*p = (-3/4) * (-3/4) = 9/16
p = 3/4

b1 and b2 are negative,
so Pearson Coefficient is -3/4
"""
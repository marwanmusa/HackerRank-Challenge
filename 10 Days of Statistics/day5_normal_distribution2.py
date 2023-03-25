"""
Task:
The final grades for a Physics exam taken by a large group of students
have a mean of μ = 70 and a standard deviation of σ = 10.
If we can approximate the distribution of these grades by a normal distribution,
what percentage of the students:
    - Scored higher than 80 (i.e., have a grade > 80)?
    - Passed the test (i.e., have a grade >= 60)?
    - Failed the test (i.e., have a grade < 60)?
Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.
"""

# Solution
import math as m

mu, sig = map(float, input().split())
t0 = float(input())
t1 = float(input())

z0 = (t0 - mu)/(sig*m.sqrt(2))
z1 = (t1 - mu)/(sig*m.sqrt(2))

print(round(100 - (100*0.5*(1+m.erf(z0))), 2))
print(round(100 - (100*0.5*(1+m.erf(z1))), 2))
print(round(100*0.5*(1+m.erf(z1)), 2))

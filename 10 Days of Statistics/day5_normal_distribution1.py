"""
Task:
In a certain plant, the time taken to assemble a car is a random variable, X,
having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
What is the probability that a car can be assembled at this plant in:
- Less than 19.5 hours?
- Between 20 and 22 hours?
"""

# Solution
import math as m

mu, sig = map(float, input().split())
t0 = float(input())
t1, t2 = map(float, input().split())

z0 = (t0 - mu)/(sig*m.sqrt(2))
z1 = (t1 - mu)/(sig*m.sqrt(2))
z2 = (t2 - mu)/(sig*m.sqrt(2))

print(round(0.5 + 0.5*m.erf(z0),3))
print(round(0.5*m.erf(z2) - 0.5*m.erf(z1),3))

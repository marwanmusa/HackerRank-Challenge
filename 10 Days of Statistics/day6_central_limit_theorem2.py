"""
Task:
The number of tickets purchased by each student for the University X vs. University Y football game
follows a distribution that has  a mean of μ = 2.4 and a standard deviation of σ = 2.0.
A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""

# Solution
import math as m

max_capacity = int(input())
n = float(input())
mu = float(input())
sig = float(input())

mu_ = n * mu
sig_ = m.sqrt(n) * sig

X = (max_capacity - mu_)/(sig_*m.sqrt(2))

print(round(0.5*(1+m.erf(X)), 4))

"""
Task:
A large elevator can transport a maximum of 9800 pounds.
Suppose a load of cargo containing 49 boxes must be transported via the elevator.
The box weight of this type of cargo follows a distribution with a mean of μ = 205 pounds
and a standard deviation of σ = 15 pounds. Based on this information,
what is the probability that all 49 boxes can be safely loaded into
the freight elevator and transported?
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

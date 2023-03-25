"""
Task:
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
- The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C(A) = 160 + 40(X^2).
- The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C(B) = 128 + 40(Y^2)..
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""

# Solution
import math

mean_A, mean_B = map(float, input().split())
cost_of_operating_A = 160 + (40 * (math.pow(mean_A, 2) + mean_A))
cost_of_operating_B = 128 + (40 * (math.pow(mean_B, 2) + mean_B))
print(round(cost_of_operating_A, 3))
print(round(cost_of_operating_B, 3))

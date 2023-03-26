"""
Task:
You have a sample of 100 values from a population with mean μ = 500 and with standard deviation σ = 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean;
in other words, compute A and B such that P(A < x < B) = 0.95.
Use the value of z = 1.96. Note that z is the z-score.
"""

# Solution
import math

sample_size = int(input())
mean_pop = float(input())
std_dev = float(input())
dist_perc = float(input())
z = float(input())

A = mean_pop - z*std_dev/math.sqrt(sample_size)
B = mean_pop + z*std_dev/math.sqrt(sample_size)

print(round(A, 2))
print(round(B, 2))

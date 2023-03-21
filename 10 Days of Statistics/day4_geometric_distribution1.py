"""
Task:
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect occurs the 5th item produced?
"""

I = list(map(int, input().split()))
n = int(input())

p = I[0]/I[1]

def geometric_distribution(n, p):
    return ((1-p)**(n-1))*p

print("%.3f" %geometric_distribution(n, p))
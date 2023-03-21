"""
Task:
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5th inspections?
"""

I = list(map(int, input().split()))
n = int(input())

p = I[0]/I[1]

def geometric_distribution(n, p):
    return ((1-p)**(n-1))*p

res = 0
for i in range(1, n+1):
    res += geometric_distribution(i, p)

print("%.3f" %res)
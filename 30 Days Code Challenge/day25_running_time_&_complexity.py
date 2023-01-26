"""
Task:
    A prime is a natural number greater than 1 that has no positive divisors
    other than 1 and itself. Given a number, n, determine and print whether
    it is Prime or Not prime.

Note:
    If possible, try to come up with a O(sqrt(n)) primality algorithm,
    or see what sort of optimizations you come up with for an O(sqrt(n)) algorithm.
"""

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors


T = int(input())
for i in range(T):
    n = int(input())
    if len(prime_factors(n)) == 1:
        print('Prime')
    else:
        print("Not prime")
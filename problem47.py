"""Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?"""

from collections import deque

from tools import prime_factors, gen_primes

primes = gen_primes(10000)
def number_factors(n):
    nod = 0
    remainder = n
    for prime in primes:
        pf = False
        while remainder % prime == 0:
            pf = True
            remainder /= prime
        nod += 1 if pf else 0
        if remainder == 1:
            return nod
    return nod

n = 1
num_consec = 0
test = 4
while num_consec < test:
    print n
    n += 1
    if number_factors(n) == test:
        num_consec += 1
    else:
        num_consec = 0
print 'The first number is %s' % (n - 3)

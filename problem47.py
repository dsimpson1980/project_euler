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

from tools import prime_factors

f = 4
factors = deque(maxlen=f)
n = 5
for x in range(f):
    n += 1
    d = [a ** b for a, b in prime_factors(n).iteritems()]
    factors.append(d)
while True:
    print n
    n += 1
    new_factors = [a ** b for a, b in prime_factors(n).iteritems()]
    factors.append(new_factors)
    if len(factors[0]) == len(factors[1]) == len(factors[2]) == len(factors[3]) == 4:
        break
print 'The first number is %s' % (n + 1 - f)

"""Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

from itertools import chain, combinations

from tools import prime_factors

def divisor_generator(n):
    factors = prime_factors(n)
    factors = [(k, v) for k, v in factors.iteritems()]
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x]
                                        for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def sum_divisors(n):
    divisors = [d for d in divisor_generator(n)]
    return sum(divisors[:-1])

total = 0
for a in range(2, 10000):
    b = sum_divisors(a)
    if a == sum_divisors(b) and a != b:
        total += a
print 'Total = %s' % total

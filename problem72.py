"""Counting fractions
Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for
d <= 1,000,000?

Solution
--------
Use a sieve to calculate phi(i) for i up to 1e6 by incrementing by multiples of
the prime in 1,...,1e6

The number of relative primes for each denominator i is the same as the number
of improper fractions we have for each denominator i.  Therefore the number of
elements in the set is the sum of phi(i) for i in 1,..,1e6
"""

limit = 1000000
phi = range(limit + 1)
result = 0
for i in xrange(2, limit + 1):
    # if we haven't encountered phi[i] yet then i is prime
    if phi[i] == i:
        # Increment the phi[j] where j has prime factor i
        for j in xrange(i, limit + 1, i):
            phi[j] = phi[j] / i * (i - 1)
    result += phi[i]
print 'Number of elements in the set = %s' % result

"""Combinatoric selections
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/(r!(n-r)!) , where r <= n, n! = nx(n-1)x...x3x2x1,and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100,
are greater than one-million?

Solution
--------

We already know 23C10 is larger than 1e6 and by symmetry we know that 23C13 is
larger than 1e6 as well giving us our first 4 numbers larger than 1e6.

We therefore know that 24C10 will be bigger than 1e6 so simply need to test if
24C9 is larger than 1e6, which it is, and then iterate through until 24C(r-1) is
less than 1e6.  This is true for 24C8 and again by symmetry we know that 24C16
is greater than 1e6 giving us our next 7 numbers.

The formula for the number greater than 1e6 is n + 1 - 2 * r for nCr the first
number greater than 1e6.
"""

def nCr(n, r):
    from math import factorial
    f = factorial
    return f(n) / f(r) / f(n - r)

r = 10
count = 0
for n in range(23, 101):
    while nCr(n, r) > 1e6:
        r -= 1
    r += 1
    count += n + 1 - 2 * r
print 'The number of nCr greater than 1e6 for 1 <= n <= 100 is %s' % count

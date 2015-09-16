"""Coin partitions
Problem 78
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

Solution
--------
This is an integer partition problem with the example given above the same as
how you many ways can you right integers summing to 5:

    5
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1

According to wikipedia the generating function for p(n) is given by:

    \sum_{n=0}^{\infinity} p(n)x^{n} = \prod_{k=1}^{\infinity}\frac{1}{1-x^{k}}

and can be written as:

    p(k) = p(k-1) + p(k-2) - p(k-5) - p(k-7) + p(k-12) + p(k-15) - p(k-22) ...

where the terms in brackets are the generalised pentagonal numbers given by
wolfram as:

     n(3n-1)/2 with n=0, +/-1, +/-2, ...,

and the signs in the rhs alternate as (-1)^m or +ve if m % 4 < 2
"""

def generalised_pentagonal_number():
    k = 1
    while True:
        yield k * (3 * k - 1) / 2
        k = -k
        yield k * (3 * k - 1) / 2
        k = -k + 1

pen_gen = generalised_pentagonal_number()
pent = [pen_gen.next()]
p, n = [1], 1
while True:
    while pent[-1] <= 10 * n:
        pent.append(pen_gen.next())
    i, value = 0, 0
    while pent[i] <= n:
        sign = 1 if i % 4 < 2 else -1
        value += sign * p[n - pent[i]]
        i += 1
    p.append(value)
    if p[-1] % 1000000 == 0:
        break
    n += 1
print 'The first value of n for which p(n) is divisible by 1,000,000 is %s' % n

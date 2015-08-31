"""Problem 64"""

from math import sqrt, floor

def fn(S, m0, d0, a0):
    m1 = d0 * a0 - m0
    d1 = (S - m1 ** 2) / d0
    a1 = floor(abs((sqrt(S) + m1) / d1))
    return m1, d1, int(a1)

count = 0
n = 10000
for S in range(2, n):
    sq = sqrt(S)
    # skip perfect squares
    if sq == int(sq):
        continue
    m = 0
    d = 1
    a = int(floor(sqrt(S)))
    a0 = a
    a_list = []
    """ condition from "On continued fractions of the square root of prime
    numbers, Alexandra Ioana Gliga, March 17, 2006"""
    while a != 2 * a0:
        m, d, a = fn(S, m, d, a)
        a_list.append(a)
    if len(a_list) % 2 == 1:
        count += 1
print 'Number of continued fractions for N <= %s with odd period = %s' % (n, count)

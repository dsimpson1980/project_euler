"""Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial

total = 0
for n in range(3, 1000000):
    if n == sum(map(factorial, [int(s) for s in str(n)])):
        print n
        total += n
print 'Sum of all numbers = %s' % total

"""Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + ^4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + ^4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

Solution
--------
We need an x digit number where x9^5 = x.  9^5 = 59049, need at least 5 digits.
5*9^5 = 295245 so we need at least 6 digits. 6*9^5 = 354294 which is the biggest
6 digit number we'll have to deal with
"""

total = 0
for n in range(2, 354295):
    sum_fifth = sum([int(d) ** 5 for d in str(n)])
    if n == sum_fifth:
        total += sum_fifth
print total

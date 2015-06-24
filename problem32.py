"""Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum."""


u = [n for n in '123456789']
v = set()
for multiplicand in range(10000):
    for multiplier in range(multiplicand, 10000):
        prod = multiplicand * multiplier
        digits = str(multiplicand) + str(multiplier) + str(prod)
        if len(digits) > 9:
            break
        elif len(digits) == 9 and sorted(digits) == u:
            v.add(prod)
print sum(v)

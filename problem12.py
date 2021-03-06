"""Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?


First calculate the prime divisors, then all divisors are combinations of these
prime divisors.  Therefore we want to determine all combination of exponents of
the divisors.  For example for,
    24 = 2^3x3^1
all divisors have the form,
    2^px3^q for p = 0, 1, 2, 3 and q = 0, 1
the number of combinations for p and q is therefore 4x2=8
"""

import numpy
from tools import prime_factors


n, total, divisors = 0, 0, 0
while divisors < 500:
    n += 1
    total += n
    factors = prime_factors(total)
    divisors = numpy.prod([f + 1 for f in factors.values()])
print total
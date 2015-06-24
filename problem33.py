"""Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

Solution
--------
Only need 2 digit numbers that have a digit that cancel, therefore start off
with two 1 digit number and add another number to the front and back and check
that it equals the original.  For integers; a,b,c:
int('a') and int('b') goes to int('ac')/int('cb')
"""

from fractions import Fraction

prod = 1
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(1, 10):
            if Fraction(a, b) == Fraction(int(str(a) + str(c)),
                                          int(str(c) + str(b))):
                prod *= Fraction(a, b)
print prod.denominator

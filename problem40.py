"""Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000"""

digit = {}
digit[1] = 1
digit[10] = 1
p = 10
old_p = 10
idx = 9
for m in range(2, 7):
    p *= 10
    d, r = divmod(p - idx, m)
    digit[p] = int(str(old_p + d)[r - 1])
    idx += 9 * old_p * m
    old_p = p
print 'product of digits = %s' % reduce(lambda x, y: x * y, digit.values())

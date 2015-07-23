"""Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Solution
--------
The example above yields a pandigital beginning with 9 so if our candidate is to
beat the example then it must also begin with a 9
The candidate must have less than 5 digits as n>1, n=2 will yield a 10 digit
concatenation.
If the candidate has 4 digits we may get a 9 digit result.  n=1 yields 4 digits
and n=2 should yield 5 digits
If the candidate has 3 digits then we would get 3+4=9 digits or 3+4+4=11 digits
If the candidate has 2 digits then we would get 2+3+3=8 or 2+3+3+3=11 digits
So our candidate must have 4 digits with n=2.
When we multiply by 2 we end up with a number 1xxxx the candidate therefore must
not contain the number 1.
We have already used the number 9 so if the multiplication by 2 ends up with a 9
then we don't have a pandigital number.  This is the case when we try 95xxx or
higher.
Obviously none of the digits in the candidate.  Therefore beginning at 9500, we
can exclude, the next lower number is 9487.
Again starting from 9100, which is excluded because of the duplicate 1, the next
largest valid candidate is 9234.
"""

u = [n for n in '123456789']
for n in range(9487, 9234, -1):
    result = str(n) + str(n * 2)
    if sorted(result) == u:
        break
print "Biggest pandigital result is %s" % result
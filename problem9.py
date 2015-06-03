"""Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solve the two formulae so we can reduce the problem to one loop with a test
condition:

a + b + c = 1e3 => c = 1e3 - a - b
a^2 + b^2 = (1e3 - a - b)^2 = 1e6 - 2e3a - 2e3b +2ab + a^2 + b^2
=> 1e6 - 2e3a - 2e3b + 2ab = 0
=> b = (2e3a - 1e6) / 2(a - 1e3)
"""

n = 1000
for a in range(1, n):
    b, remainder = divmod(2e3 * a - 1e6, 2 * (a - 1e3))
    if b > 0 and remainder == 0:
        break
c = n - a - b
print 'abc = %s' % (a * b * c)
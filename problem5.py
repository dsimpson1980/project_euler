"""Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"""

def prime_factors(x):
    factors, d = {}, 2
    while d <= x:
        if x % d == 0:
            x /= d
            factors[d] = factors.get(d, 0) + 1
        else:
            d += 1
    return factors

biggest_factor = {}
for n in range(1, 21):
    for factor, multiple in prime_factors(n).iteritems():
        if multiple > biggest_factor.get(factor, 0):
            biggest_factor[factor] = multiple
result = 1
for factor, multiple in biggest_factor.iteritems():
    result *= factor ** multiple
print result

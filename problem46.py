"""Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?"""

from tools import gen_primes

s, squares = 1, [1]
prime_generator = gen_primes()
primes = [prime_generator.next()]
n = 7
while True:
    n += 2
    while n > squares[-1]:
        s += 1
        squares.append(s ** 2)
    while n > primes[-1]:
        primes.append(prime_generator.next())
    if n == primes[-1]:
        continue
    test = False
    square = 0
    for square in squares:
        if n - 2 * square in primes:
            test = True
            break
    if not test:
        break
print 'Failed for %s' % n

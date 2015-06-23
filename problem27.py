"""Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, -79 and
1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

Solution
--------
The first number generated for n=0 is b so b must be prime.  Therefore we should
only be using values of b that are prime.
The second number generated for n=1 has the form 1 + a + b.  For this to be
prime a + b must be even.

"""

from tools import gen_primes

def is_prime(candidate, primes):
    idx = 0
    while primes[idx] <= candidate:
        if primes[idx] == candidate:
            return True
        idx += 1
    return False

prime_generator = gen_primes()
primes1000, p = [], prime_generator.next()
while p < 1000:
    primes1000.append(p)
    p = prime_generator.next()
primes = list(primes1000)
while p < 1000000:
    primes.append(p)
    p = prime_generator.next()
max_a, max_b, max_seq = 0, 0, 0
for a in range(-999, 1000):
    for b in primes1000:
        if a + b % 2 == 1:
            continue
        n = 0
        while is_prime(abs(n * n + a * n + b), primes):
            n += 1
        if n > max_seq:
            max_prod = a * b
            max_seq = n
print max_prod
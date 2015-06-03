"""Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from tools import gen_primes

prime_generator = gen_primes()
prime, total = 0, 0
while prime < 2e6:
    total += prime
    prime = prime_generator.next()
print total
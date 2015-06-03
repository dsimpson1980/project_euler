"""10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?"""

from tools import gen_primes


prime_generator = gen_primes()
for n in range(1, 10002):
    prime = prime_generator.next()
print prime
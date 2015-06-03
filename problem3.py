"""Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from math import sqrt

from tools import gen_primes


n = 600851475143.
largest_prime_limit = sqrt(n)
for prime in gen_primes():
    if prime > largest_prime_limit:
        break
    if n % prime == 0:
        largest_prime = prime
print largest_prime
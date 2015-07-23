"""Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

from tools import gen_primes

prime_generator = gen_primes()
primes = {prime_generator.next(): True for n in range(1000000)}
appends = [1, 2, 3, 5, 7, 9]
candidates = [3, 7]
truncated_primes = []
prime_generator = gen_primes()
count, total = 0, 0
while count < 11:
    candidate = candidates[0]
    candidates = candidates[1:]
    if primes.get(candidate, False):
        is_truncatable = True
        n = candidate
        multiplier = 1
        while n > 0:
            is_truncatable = primes.get(n, False) and is_truncatable
            n /= 10
            multiplier *= 10
        if is_truncatable and candidate > 10:
            total += candidate
            count += 1
        for i in range(len(appends)):
            candidates.append(multiplier * appends[i] + candidate)
print total
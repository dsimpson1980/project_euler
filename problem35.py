"""Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

Solution
--------
Any primes containing a 2 or a 5 cannot be a circular prime, except the numbers
2 and 5.  Otherwise a rotation would be even or would end in a 5, making it
divisible by 5.

This cuts he number of primes to be tested down from 78499 to be 1111 (assuming
2 and 5 are not tested)
"""

from tools import gen_primes

prime, primes = 1, {2: False, 5: False}
circular_primes = {}
prime_generator = gen_primes()
while prime < 1000000:
    prime = prime_generator.next()
    if all([int(p) % 2 == 1 and int(p) != 5 for p in str(prime)]):
        primes[prime] = False
for prime in primes.keys():
    prime_str = str(prime)
    cycles = [int(prime_str[i:] + prime_str[:i]) for i in range(len(prime_str))]
    if all([p in primes for p in cycles]):
        for p in cycles:
            circular_primes[p] = True
result = circular_primes.keys()
result.sort()
print 'Number of circular primes: %s' % len(result)

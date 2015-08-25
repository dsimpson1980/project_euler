"""Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?"""

from tools import gen_primes

prime_generator = gen_primes()
prime = prime_generator.next()
primes, cumsum_primes = {prime: True}, {0: 0, 1: prime}
num_primes = 1
while prime < 1e6:
    num_primes += 1
    prime = prime_generator.next()
    primes[prime] = True
    cumsum_primes[num_primes] = cumsum_primes[num_primes-1] + prime
limit = 1e6
count = 1
result = 2
for i in range(0, num_primes):
    for j in range(i - (count + 1), -1, -1):
        if cumsum_primes[i] - cumsum_primes[j] > limit:
            break
        if cumsum_primes[i] - cumsum_primes[j] in primes:
            count = i - j
            result = cumsum_primes[i] - cumsum_primes[j]
print 'Prime made up of the most number of consecutive primes is %s with %s primes' % (result, count)

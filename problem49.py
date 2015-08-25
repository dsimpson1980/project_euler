"""Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?"""

from tools import gen_primes

prime_generator = gen_primes()
prime = 0
while prime < 1e3:
    prime = prime_generator.next()
primes = []
grouped_primes = {}
while prime < 1e4:
    primes.append(prime)
    prime = prime_generator.next()
    key = int(''.join(sorted(str(prime))))
    grouped_primes.setdefault(key, []).append(prime)
for k, v in grouped_primes.iteritems():
    if k == 1478:
        continue
    for n in range(len(v) - 1):
        for m in range(n + 1, len(v)):
            if 2 * v[m] - v[n] in v:
                print 'Number is %s%s%s' % (v[n], v[m], 2 * v[m] - v[n])

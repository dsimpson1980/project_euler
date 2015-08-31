"""Prime digit replacements
Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family."""

from itertools import combinations

from tools import gen_primes

primes = gen_primes(1e6)

def replace(x, replace_pattern):
    x = str(x)
    count = 0
    first_prime = None
    for j in range(10):
        y = [j] * 6
        for n, idx in enumerate(replace_pattern):
            y[idx] = int(x[n])
        y = int(''.join(map(str, y)))
        if y in primes:
            if first_prime is None:
                first_prime = y
            count += 1
        if j - count > 2:
            break
    return count, first_prime

first_prime = None
for pattern in combinations(range(6), 3):
    for x in range(100, 999):
        count, prime = replace(x, pattern)
        if count == 8:
            first_prime = prime
            break
    else:
        continue
    break
print 'first prime = %s' % first_prime

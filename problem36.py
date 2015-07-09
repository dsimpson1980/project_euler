"""Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Solution
--------
If we generate palindromic numbers then we don't need to check for them.
Generating using numbers by taking numbers in range(100), reversing them and
sticking them together gives us palindromes of even length.  Doing the same
thing but adding the number 0-9 in between the original and reversal gives us
all the even length palindromes.
Then using the numbers in range(100, 1000) and doing the same reversal and
append yields the remaining palindromes

This cuts the number of palindromes to be checked down to 1998
"""
def is_palindrome(candidate):
    candidate = str(candidate)
    n, odd = divmod(len(candidate), 2)
    for m in range(n):
        if candidate[n - 1 - m] != candidate[n + m + odd]:
            return False
    return True

def palindromes():
    for n in range(1, 10):
        yield n
    for n in range(1, 100):
        yield int(str(n) + str(n)[::-1])
        for m in range(10):
            yield int(str(n) + str(m) + str(n)[::-1])
    for n in range(100, 1000):
        yield int(str(n) + str(n)[::-1])

total = 0
for n in palindromes():
    if is_palindrome(bin(n)[2:]):
        total += n
print'Total of palindromes in base 10 and 2 is %s' % total

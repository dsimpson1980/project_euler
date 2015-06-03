"""Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def find_divisor():
    for n in range(999, 99, -1):
        palindrome = int(str(n) + str(n)[::-1])
        for d in range(999, 99, -1):
            if palindrome % d == 0:
                if palindrome / d < 1000:
                    return palindrome
print find_divisor()
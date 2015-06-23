"""Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers."""


from tools import divisor_generator

def sum_divisors(n):
    divisors = [d for d in divisor_generator(n)]
    return sum(divisors[:-1])

limit = 28123
abundant_numbers = [n for n in range(12, limit + 1) if sum_divisors(n) > n]
sum_two_abundent = [False] * limit
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        if abundant_numbers[i] + abundant_numbers[j] < limit:
            sum_two_abundent[abundant_numbers[i] + abundant_numbers[j]] = True
print sum([n for n, v in enumerate(sum_two_abundent) if not v])

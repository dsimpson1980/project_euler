"""Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

n = 100
sum_squares = n * (n + 1) * (2 * n + 1) / 6
square_sum = (n * (1 + n) / 2) ** 2
sum_square_difference = square_sum - sum_squares
print sum_square_difference
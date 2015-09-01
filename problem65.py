"""Problem 65"""

num_terms = 100
d, n = 1, 2
for i in range(2, num_terms + 1):
    n, d = (2 * (i / 3) if i % 3 == 0 else 1) * n + d, n
total = 0
for s in str(n):
    total += int(s)
print 'Sum of the digits of the numerator = %s' % total

"""Self powers
Problem 48
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000."""

result = 0
modulo = 10000000000
for i in range(1, 1001):
    result += reduce(lambda x, y: x*y % modulo, [i]*i)
    result %= modulo
print 'The last 10 digits are %s' % result

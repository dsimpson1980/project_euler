"""Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
"""

import math

def is_pentagonal(x):
    y = (1 + math.sqrt(1 + 24 * x)) / 6
    return y == int(y)

def main():
    not_found, D, i = True, None, 0
    pentagonals, l = {}, {}
    while not_found:
        i += 1
        n = i * (3 * i - 1) / 2
        pentagonals[i] = n
        l[n] = i
        for j in range(i - 1, 0, -1):
            m = pentagonals[j]
            if is_pentagonal(n - m) and is_pentagonal(n + m):
                D = abs(n - m)
                not_found = False
    return D

if __name__ == '__main__':
    D = main()
    print "D = %s" % D

"""The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1);
so the first ten triangle numbers are:1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t_{10}. If the word value is a
triangle number then we shall call the word a triangle word."""

import csv

class TriangularNumbers(object):
    def __init__(self):
        self.numbers = {1: True}
        self.n = 1
        self.largest_value = 1

    def next(self):
        return self.gen().next()

    def gen(self):
        self.n += 1
        self.largest_value = 0.5 * self.n * (self.n + 1)
        self.numbers[self.largest_value] = True
        yield self.largest_value

def word_value(word):
    total = 0
    for c in word:
        total += ord(c) - 64
    return total

words = []
with open('data/words.txt') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        words += line
tri_gen = TriangularNumbers()
count = 0
for word in words:
    value = word_value(word)
    while value > tri_gen.largest_value:
        tri_value = tri_gen.next()
    if value in tri_gen.numbers:
        count += 1
print 'Number of triangular words = %s' % count
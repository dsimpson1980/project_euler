"""Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

Solution
--------
For any given p we must have a + b + c = p => c = p - b - a where c is the
hypotenuse.
We therefore also have a^2 + b^2 = c^2
Using this method we'll be counting all permutations twice but it will not
affect the comparison between different p
"""

max_count, max_p = 0, 0
for p in range(3, 1001):
    count = 0
    for a in range(1, p / 2):
        b, r = divmod(2 * a * p - p * p, 2 * (a - p))
        if r == 0:
            count += 1
    if count > max_count:
        max_count, max_p = count, p
print 'p = %s has the most combinations' % max_p
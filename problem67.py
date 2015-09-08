"""Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)

Solution
--------
Same as problem 18 but need to read data from triangle.txt"""

data = []
with open('data/triangle.txt', 'r') as f:
    for row in f.readlines():
        data.append(map(int, row.rstrip().split(' ')))
print data
for row_num in range(len(data) - 2, -1, -1):
    for i in range(len(data[row_num])):
        data[row_num][i] += max(data[row_num + 1][i], data[row_num + 1][i + 1])
print 'Max total = %s' % data[0][0]

"""Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form
16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
5-gon ring?

Solution
--------
Brute force, check for all permutations and that the 5 lines all sum to the same
total
Indexing for each line is as follows:
0, 1, 2
3, 2, 4
5, 4, 6
7, 6, 8
9, 8, 1

For the solution to have 16 digits, 10 must appear in one of the petals/start of
the line; 0, 3, 5, 7, 9 i.e. not in the inner ring

Indexing starts with the smallest number in each of the petals.  Therefore if
any of the numbers in positions 3, 5, 7, and 9 are greater than that in position
0 then we should discard the permutation
"""

from itertools import permutations

lines = [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]

def check_solution(p):
    # Check 10 is not on the inner ring
    if 10 in p[2::2] + (p[1],):
        return False
    # Discard the permutation is numbering is not beginning with the smallest petal
    for n in range(3, 10, 2):
        if p[0] > p[n]:
            return False
    # Check the totals all match
    total = p[lines[0]] + p[lines[1]] + p[lines[2]]
    for n in range(4):
        if p[lines[n * 3]] + p[lines[n * 3 + 1]] + p[lines[n * 3 + 2]] != total:
            return False
    return True

total = 0
for p in permutations(range(1, 11)):
    if check_solution(p):
        sub_total = ''.join([str(p[x]) for x in lines])
        total = max(total, sub_total)
print 'Maximum 16 digit number is %s' % total
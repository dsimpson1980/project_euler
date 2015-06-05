"""Lattice paths
Problem 15
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?


Using combinatorics; for an nxn grid there will always be n downs and n rights
to get to the bottom right.  Since all the downs are set if we have already
chosen the rights then we have the problem n choose 2n
"""

grid_size = 20
routes = 1
for n in range(1, grid_size + 1):
    routes *= 2 * grid_size - n + 1
    routes /= n
print routes
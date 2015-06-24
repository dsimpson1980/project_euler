"""Coin sums
Problem 31
In England the currency is made up of pounds and pence and there are eight coins
in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 pounds (100p) and 2 pounds (200p).
It is possible to make 2 pounds in the following way:

1x1pound + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 pound be made using any number of coins?
"""

target = 200
ways = {0: 1}
coins = [1, 2, 5, 10, 20, 50, 100, 200]
for n in range(len(coins)):
    for m in range(coins[n], target + 1):
        ways[m] = ways.get(m, 0) + ways[m - coins[n]]
print ways[200]

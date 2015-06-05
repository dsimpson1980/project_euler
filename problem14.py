"""Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


cache = {1: 1}
max_seq_len, best_start_num = 0, 0
for n in range(2, 1000001):
    seq, k = n, 0
    while seq != 1 and seq >= n:
        k += 1
        seq = seq / 2 if seq % 2 == 0 else seq * 3 + 1
    cache[n] = k + cache[seq]
    if cache[n] > max_seq_len:
        max_seq_len = cache[n]
        best_start_num = n
print best_start_num, max_seq_len
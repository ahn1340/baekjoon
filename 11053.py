"""
Author: Jin woo Ahn
백준 11053번 (가장 긴 증가하는 부분 수열) 
"""

n = int(input())
seq = list(map(int, input().split()))

# O(n^2) solution
def longest_subsequence(seq, n):
    memo = {0: 1}
    for i in range(1, n):
        candidates = [1]
        for j in range(0, i):
            if seq[i] > seq[j]:
                candidates.append(memo[j] + 1)
        longest = max(candidates)
        memo[i] = longest

    return max(memo.values())

print(longest_subsequence(seq, n))

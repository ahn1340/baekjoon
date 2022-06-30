"""
Author: Jin Woo Ahn
백준 15649번 (N과 M)
"""


import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

def backtracking(n, m):
    nums = [i for i in range(1, n+1)]
    start = []
    recursion(start, nums, m)

def recursion(curr, options, m):
    if is_solution(curr, m):
        print(" ".join([str(c) for c in curr]))
        return
    elif len(curr) == m:
        return

    for i in range(len(options)):
        c = curr[:]
        op = options[:]
        c.append(op.pop(i))

        recursion(c, op, m)
    

def is_solution(seq, m):
    if len(seq) == m:
        if len(seq) == len(set(seq)):
            return True

backtracking(n, m)

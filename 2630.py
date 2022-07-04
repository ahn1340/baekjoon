"""
Author: Jin Woo Ahn
백준 2630번 (색종이 만들기)
"""
import sys
N = int(sys.stdin.readline())
paper = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    paper.append(row)
# solve
def solve(paper):
    memo = [0, 0]  # 0, 1
    recursion(paper, memo)
    for i in memo:
        print(i)

def recursion(paper, memo):
    n = len(paper)
    start = paper[0][0]
    if is_same(paper, start):
        memo[start] += 1
    else:
        # cut paper
        for i in range(2):
            for j in range(2):
                length = n // 2
                subpaper = paper[length*i:length*(i+1)]  # select rows
                subpaper = [row[length*j:length*(j+1)] for row in subpaper]  # select columns
                recursion(subpaper, memo)

def is_same(paper, start):
    n = len(paper)
    for i in range(n):
        for j in range(n):
            if paper[i][j] != start:
                return False
    return True

solve(paper)

"""
Author: Jin Woo Ahn
백준 1780번 (종이 자르기)
"""
# parse
N = int(input())

paper = []
for i in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

    # solve
def solution(paper):
    count = [0, 0, 0]  # -1, 0, 1
    recursion(paper, count)
    for c in count:
        print(c)

def recursion(paper, count):
    n = len(paper)
    if is_same(paper, n):
        val = paper[0][0]
        count[val+1] += 1
    else:
        nn = n // 3
        for i in range(3):
            for j in range(3):
                subpaper = paper[i*nn:(i+1)*nn]
                subpaper = [line[j*nn:(j+1)*nn] for line in subpaper]
                recursion(subpaper, count)

def is_same(paper, n):
    if n == 1:
        return True
    compare = paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != compare:
                return False
    return True
    
solution(paper)

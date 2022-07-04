"""
Author: Jin Woo Ahn
백준 1697번 (숨바꼭질)
BFS사용하여 최소거리 탐색
"""

from collections import deque

N, K = list(map(int, input().split()))

def get_next(curr):
    nexts = []
    if curr > 0:
        nexts.append(curr - 1)
    if curr < 100000:
        nexts.append(curr + 1)
    if curr <= 50000:
        nexts.append(curr * 2)

    return nexts

def bfs(start, end):
    if start >= end:
        return start - end
    queue = deque()
    step_queue = deque()
    in_queue = {}
    curr = start
    queue.append(curr)
    step_queue.append(0)
    in_queue[curr] = True
    while queue:
        curr = queue.popleft()
        curr_step = step_queue.popleft()
        if curr == end:
            return curr_step
        nexts = get_next(curr)
        for next in nexts:
            if next not in in_queue:
                in_queue[next] = True
                queue.append(next)
                step_queue.append(curr_step + 1)

print(bfs(N, K))

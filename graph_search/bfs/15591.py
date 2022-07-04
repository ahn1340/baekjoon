"""
Author: Jin Woo Ahn
백준 15591번 문제
"""

from collections import deque

n, q = list(map(int, input().split()))

graph = {}
for i in range(n-1):
    n1, n2, r = list(map(int, input().split()))
    if not n1 in graph:
        graph[n1] = [[n2, r]]
    else:
        graph[n1].append([n2, r])
    if not n2 in graph:
        graph[n2] = [[n1, r]]
    else:
        graph[n2].append([n1, r])

def bfs(graph, n, K, start):
    visited = [False for i in range(n+1)]
    queue = deque()
    root = [start, 0]
    queue.append(root)
    counter = 0
    
    while queue:
        curr = queue.popleft()
        if not visited[curr[0]]:
            if curr[1] >= K and not curr == root:
                counter += 1
            visited[curr[0]] = True
            next = []
            neighbors = graph[curr[0]]
            for n in neighbors:
                if n[1] >= K:
                    next.append(n)
            queue.extend(next)
    
    return counter

for i in range(q):
    K, start = list(map(int, input().split()))
    print(bfs(graph, n, K, start))
                    

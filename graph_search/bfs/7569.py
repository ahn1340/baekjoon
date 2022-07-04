"""
백준 7569번 (토마토)
3차원 bfs문제
"""
import sys
from copy import deepcopy

M, N, H = list(map(int, sys.stdin.readline().split()))
box = []  # (h, y, x)
for i in range(H):
    floor = []
    for j in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        floor.append(row)
    box.append(floor)

def solution(box):
    H, Y, X = len(box), len(box[0]), len(box[0][0])
    ripe = {}
    not_ripe = {}
    empty = {}
    for h in range(H):
        for y in range(Y):
            for x in range(X):
                if box[h][y][x] == 1:
                    ripe[(h, y, x)] = True
                elif box[h][y][x] == 0:
                    not_ripe[(h, y, x)] = True

    counter = 0
    while True:
        riped = ripe_neighbors(box, ripe, not_ripe, (H, Y, X))
        if not riped:
            if len(not_ripe) == 0:
                print(counter)
                break
            else:
                print(-1)
                break
        counter += 1

def ripe_neighbors(box, ripe, not_ripe, size):
    H, Y, X = size[0], size[1], size[2]
    dhs, dys, dxs = [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0]
    ripe_copy = deepcopy(ripe)
    riped = False  # True at least one tomato riped
    for idx in ripe_copy.keys():
        del ripe[idx]  # remove from ripe dict (makes computation efificient)
        h, y, x = idx[0], idx[1], idx[2]
        for dh, dy, dx in zip(dhs, dys, dxs):
            nh = h + dh
            ny = y + dy
            nx = x + dx
            if not (nh < 0 or nh >= H or ny < 0 or ny >= Y or nx < 0 or nx >= X):  # if not out of bounds
                cand = (nh, ny, nx)
                if cand in not_ripe:
                    del not_ripe[cand]  # remove from not ripe dict
                    ripe[cand] = True  # add to ripe dict
                    riped = True
    return riped
                    
solution(box)

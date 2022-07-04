"""
백준 14500번 (테트로미노)
브루트포스 
"""
import sys
N, M = list(map(int, sys.stdin.readline().split()))

paper = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    paper.append(row)

def get_tetrominos():
    # get all possible tetromino configurations
    tets = []
    tet1 = [(0, 0), (0, -1), (0, 1), (-1, 0)]  # hat
    tet2 = [(0, 0), (-1, -1), (0, -1), (1, 0)]  # stair
    tet3 = [(0, 0), (-1, 0), (1, 0), (1, 1)]  # gun
    tet4 = [(0, 0), (1, 0), (0, 1), (1, 1)]  # box
    tet5 = [(0, 0), (0, 1), (0, 2), (0, 3)]  # bar
    tets.extend([tet1, tet2, tet3, tet4, tet5])
    # flip: stair, gun, bar
    tet2_t = transpose(tet2)
    tet3_t = transpose(tet3)
    tet5_t = transpose(tet5)
    tets.extend([tet2_t, tet3_t, tet5_t])
    # rotate: hat, stair(transposed), gun(transposed)
    for tet in ([tet1, tet2, tet3, tet2_t, tet3_t]):
        for i in range(3):
            tet = rotate90(tet)
            tets.append(tet)
    return tets
        
def rotate90(tetromino):
    rotate_dict = {(-1, -1): (-1, 1),
                   (-1, 0): (0, 1),
                   (-1, 1): (1, 1),
                   (0, 1): (1, 0),
                   (1, 1): (1, -1),
                   (1, 0): (0, -1),
                   (1, -1): (-1, -1),
                   (0, -1): (-1, 0),
                   (0, 0): (0, 0)
                  }
    tet90 = []
    for idx in tetromino:
        tet90.append(rotate_dict[idx])
    return tet90

def transpose(tetromino):
    tet_t = []
    for idx in tetromino:
        tet_t.append((idx[1], idx[0]))
    return tet_t

def search(paper, N, M):
    maximum = -1
    tets = get_tetrominos()
    for tet in tets:
        for i in range(N):
            for j in range(M):
                sum = 0
                for idx in tet:
                    n, m = idx[0] + i, idx[1] + j
                    if not (n < 0 or n >= N or m < 0 or m >= M):  # if not out of bounds:
                        sum += paper[n][m]
                    else:
                        break
                if sum > maximum:
                    maximum = sum
    return maximum

print(search(paper, N, M))

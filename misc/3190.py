def parse_input():
    """
    parse inputs
    """
    N = int(input())
    K = int(input())
    # world[r][c][0] -> -1 if empty, -2 if apple, one of [0, 1, 2, 3] (left up, right, down) if snake body
    world = [[-1 for _ in range(N)] for _ in range(N)]
    # put apples in the world
    for i in range(K):
        r, c = list(map(int, input().split()))
        world[r-1][c-1] = -2
    L = int(input())
    # get snake path
    path = []
    for i in range(L):
        X, C = list(input().split())
        X = int(X)
        path.append((X, C))
    world[0][0] = 2  # initial snake position and orientation
    
    return N, K, L, world, path


def move_snake(world, head, tail, N):
    """
    Move snake one step, return new world, head and tail of snake, and flag if collided
    """
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    # get snake's direction and move one step
    hr, hc = head
    tr, tc = tail
    hd = world[hr][hc]  # head direction
    assert hd >= 0
    # stretch head
    nhr, nhc = hr + dr[hd], hc + dc[hd]  # new head r, new head c
    # check if collided with wall
    if not (0 <= nhr < N and 0 <= nhc < N):
        return head, tail, True
    # check if collided with body
    if world[nhr][nhc] >= 0:
        return head, tail, True
    # if not collided
    if world[nhr][nhc] == -1:  # empty space
        td = world[tr][tc]  # tail direction
        ntr, ntc = tr + dr[td], tc + dc[td]  # new tail
        # where tail was becomes empty space
        tail = (ntr, ntc)
        world[tr][tc] = -1
    # space becomes snake head
    head = (nhr, nhc)
    world[nhr][nhc] = hd

    return head, tail, False


def change_direction(world, head, direction):
    """
    Change head's direction
    """
    assert direction in ['L', 'D']  # left, right
    hr, hc = head  # head r, head c
    hd = world[hr][hc]  # head direction
    # compute new head direction
    if direction == 'L':
        hd = (hd - 1) % 4
    elif direction == 'D':
        hd = (hd + 1) % 4
    # update head direction
    world[hr][hc] = hd
        

def main():
    N, K, L, world, path = parse_input()
    head = (0, 0)
    tail = (0, 0)

    ci = 0  # change index
    counter = 0
    for i in range(1, 10001):
        counter += 1
        head, tail, collided = move_snake(world, head, tail, N)
        # return if collided
        if collided:
            return counter
        # change direction
        if ci < len(path):
            if i == path[ci][0]:
                direction = path[ci][1]
                change_direction(world, head, direction)
                ci += 1

    return counter

print(main())

# parse input
M, S = list(map(int, input().split()))
# world[r][c][0]: dict of orientations of fishes, world[r][c][1]: 0 if normal, 2 if smell in current round, 1 if smell in previous round
world = [[[{k: 0 for k in range(1, 9)}, 0] for j in range(4)] for i in range(4)]
for i in range(M):
    r, c, direction = list(map(int, input().split()))
    world[r-1][c-1][0][direction] += 1

r, c = list(map(int, input().split()))
shark_pos = (r-1, c-1)

# for updating direction
d_dict = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

def get_movable_grid(world, pos, direction, shark_pos):
    """
    given current position and direction, compute first movable cell and new direction.
    If no movable cell, return current position
    """
    new_pos = pos
    new_d = direction
    for _ in range(8):
        _, d_cand = divmod(direction, 8)  # candidate direction
        if d_cand == 0:
            d_cand = 8
        # check if position is movable
        x, y = pos
        dx, dy = d_dict[d_cand]
        nx, ny = x + dx, y + dy
        if (0 <= nx < 4) and (0 <= ny < 4):  # check if new_pos not out of bound
            if (nx, ny) != shark_pos and world[nx][ny][1] == 0:  # check if new_pos has no smell nor shark
                new_pos = (nx, ny)
                new_d = d_cand
                break  # movable position found
        
        direction -= 1

    return new_pos, new_d


def move_fishes(world, shark_pos):
    """
    given current world state, move fishes to a new state
    """
    new_world = [[[{k: 0 for k in range(1, 9)}, 0] for j in range(4)] for i in range(4)]
    # iterate through the world
    for r in range(4):
        for c in range(4):
            for d in range(1, 9):  # direction
                n_fishes = world[r][c][0][d]
                if n_fishes > 0:  # if any fish is looking in that direction
                    (nr, nc), new_d = get_movable_grid(world, (r, c), d, shark_pos)
                    new_world[nr][nc][0][new_d] += n_fishes
    return new_world


def compute_shark_path(world, shark_pos, step):
    """
    given current world and shark position, compute the optimal shark path using DFS
    """
    pass
    #TODO: implement this

import copy

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
            # update smell
            new_world[r][c][1] = world[r][c][1]
    return new_world


def get_score(world, pos):
    """
    given current world and position, compute the number of fishes in that position
    """
    score = 0
    for i in range(1, 9):
        score += world[pos[0]][pos[1]][0][i]
    return score
    

def move_shark(world, shark_pos, step):
    """
    given current world and shark position, compute shark's new position and grids that smell
    """
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    sr0, sc0 = shark_pos
    max_score = -float('inf')
    max_path = None
    new_shark_pos = None

    # compute shark's path and grids that smell
    for i, (dr1, dc1) in enumerate(zip(dr, dc)):
        visited = []  # visited grids
        sr1, sc1 = sr0 + dr1, sc0 + dc1
        if 0 <= sr1 < 4 and 0 <= sc1 < 4:  # check if grid valid
            score1 = get_score(world, (sr1, sc1))  # score of first grid
            visited.append((sr1, sc1))
            
            for j, (dr2, dc2) in enumerate(zip(dr, dc)):
                sr2, sc2 = sr1 + dr2, sc1 + dc2
                if 0 <= sr2 < 4 and 0 <= sc2 < 4:  # check if grid valid
                    if (sr2, sc2) not in visited:
                        score2 = get_score(world, (sr2, sc2))  # score second grid
                    else:
                        score2 = 0
                    visited.append((sr2, sc2))
                    
                    for k, (dr3, dc3) in enumerate(zip(dr, dc)):
                        sr3, sc3 = sr2 + dr3, sc2 + dc3
                        if 0 <= sr3 < 4 and 0 <= sc3 < 4:  # check if grid valid
                            if (sr3, sc3) not in visited:
                                score3 = get_score(world, (sr3, sc3))  # score of third grid
                            else:
                                score3 = 0
                            visited.append((sr3, sc3))
                            
                            # compute final score and update
                            score = score1 + score2 + score3
                            if max_score < score:
                                max_score = score
                                new_shark_pos = (sr3, sc3)
                                # get smelly grids
                                smelly_grids = []
                                if score1 > 0:
                                    smelly_grids.append((sr1, sc1))
                                if score2 > 0:
                                    smelly_grids.append((sr2, sc2))
                                if score3 > 0:
                                    smelly_grids.append((sr3, sc3))
                            # remove sr3, sc3
                            visited.pop()
                    # remove sr2, sc2
                    visited.pop()
            # remove sr1, sr2
            visited.pop()
                    
    
    # remove fishes from smelly grids
    for (r, c) in smelly_grids:
        for i in range(1, 9):
            world[r][c][0][i] = 0
              
    return world, new_shark_pos, smelly_grids


def update_smell(world, smelly_grids):
    """
    Update smell of each grid
    """
    # make smell less
    for r in range(4):
        for c in range(4):
            if world[r][c][1] > 0:
                world[r][c][1] -= 1
    # update fresh smell
    for (r, c) in smelly_grids:
        world[r][c][1] = 2

    return world


def copy_fishes(old_world, new_world):
    """
    Copy fishes from old world
    """
    for r in range(4):
         for c in range(4):
             for i in range(1, 9):
                 new_world[r][c][0][i] += old_world[r][c][0][i]

    return new_world


def compute_num_fishes(world):
    """
    Compute total number of fishes in current world state
    """
    count = 0
    for r in range(4):
        for c in range(4):
            for i in range(1, 9):
                count += world[r][c][0][i]
    return count
                

def main(world, shark_pos, S):
    for i in range(S):
        old_world = copy.deepcopy(world)
        world = move_fishes(world, shark_pos)
        world, shark_pos, smelly_grids = move_shark(world, shark_pos, 1)
        world = update_smell(world, smelly_grids)
        world = copy_fishes(old_world, world)

    count = compute_num_fishes(world)
    print(count)

main(world, shark_pos, S)

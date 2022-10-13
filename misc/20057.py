def traverse(board):
    r, c = N // 2, N // 2  # initial position
    # left, down, right, up
    drs = [0, 1, 0, -1]
    dcs = [-1, 0, 1, 0]
    # two turns, then increment
    steps = 1  # number of movements in one direction
    direction = 0  # direction of movement
    total_s_out = 0
    for i in range(N - 1):  # i * two turns
        times = 2 if i < N - 2 else 3
        for _ in range(times):
            dr, dc = drs[direction % 4], dcs[direction % 4]
            for _ in range(steps):
                r, c = r + dr, c + dc  # new position
                s_out = compute_new_board(board, (r, c), direction % 4)
                total_s_out += s_out
            direction += 1  # change direction
        steps += 1

    return total_s_out


def rotate(vec, direction):
    """
    rotate vectors counter-clockwise
    direction: one of [0, 1, 2, 3]
    """
    r, c = vec
    for i in range(direction):
        r, c = -c, r 
    return (r, c)


def compute_new_board(board, shark_pos, direction):
    """
    compute new board state and return amount of sand blown out from current movement
    """
    vecs_r = [-1, 1, -1, 1, -2, 2, -1, 1, 0, 0]
    vecs_c = [1, 1, 0, 0, 0, 0, -1, -1, -2, -1]
    ratios = [1, 1, 7, 7, 2, 2, 10, 10, 5, 0]
    
    r, c = shark_pos
    val = board[r][c]  # amount of sand at current position
    board[r][c] = 0
    s_out = 0  # amount blown out of board
    s_in = 0  # amount blown to another grid
    for vr, vc, ratio in zip(vecs_r, vecs_c, ratios):
        vr, vc = rotate((vr, vc), direction)
        nr, nc = r + vr, c + vc  # position to which sand will be blown
        inb = 0 <= nr < N and 0 <= nc < N  # in bound, boolean
        # blow remaining sand to alpha
        if ratio == 0:
            blown = val - s_out - s_in
        else:
            blown = int(val * (ratio / 100))  # amount blown to this grid
        if inb:
            board[nr][nc] += blown
            s_in += blown
        else:
            s_out += blown

    return s_out
            

#### main part ####
N = int(input())

board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)           

print(traverse(board))

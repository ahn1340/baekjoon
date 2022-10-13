def move_clouds(clouds, move):
    """
    move clouds to speficied direction
    move: [direction, steps]
    """
    drs = [0, -1, -1, -1, 0, 1, 1, 1]
    dcs = [-1, -1, 0, 1, 1, 1, 0, -1]
    new_clouds = []
    d, s = move[0] - 1, move[1]  # minus one to directions to make them indices
    for r, c in clouds:
        nr, nc = (r + drs[d] * s) % N, (c + dcs[d] * s) % N
        new_clouds.append((nr, nc))
    return set(new_clouds)


def rain(board, clouds):
    for r, c in clouds:
        board[r][c] += 1


def copy_bug(board, clouds):
    drs = [-1, -1, 1, 1]
    dcs = [1, -1, 1, -1]
    for r, c in clouds:
        counter = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] > 0:
                    counter += 1
        board[r][c] += counter


def get_new_clouds(board, clouds):
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r, c) not in clouds:
                new_clouds.append((r, c))
                board[r][c] -= 2
    return set(new_clouds)


def compute_sum(board):
    total = 0
    for r in range(N):
        for c in range(N):
            total += board[r][c]
    return total

#### main part ####
N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

moves = []
for _ in range(M):
    move = list(map(int, input().split()))
    moves.append(move)

# initial cloud positions
clouds = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
    
for move in moves:
    clouds = move_clouds(clouds, move)
    rain(board, clouds)
    copy_bug(board, clouds)
    clouds = get_new_clouds(board, clouds)

print(compute_sum(board))

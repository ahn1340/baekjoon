N = int(input())
board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)


def execute_move(board, direction):
    """
    given direction, compute result of the board
    """
    new_board = [[] for i in range(N)]
    for i in range(N):  # global variable
        new_line = []
        if direction == 'left':
            prev = board[i][0]
        elif direction == 'right':
            prev = board[i][-1]
        elif direction == 'up':
            prev = board[0][i]
        else:
            prev = board[-1][i]
        
        for j in range(1, N):
            if direction == 'left':
                curr = board[i][j]
            elif direction == 'right':
                curr = board[i][-(j+1)]
            elif direction == 'up':
                curr = board[j][i]
            else:
                curr = board[-(j+1)][i]
            # if curr is 0, i.e. empty space, skip
            if curr == 0:
                continue
            if prev is None:  # prev has been merged with another block
                prev = curr
            elif curr == prev:  # prev should be merged with curr
                prev = None
                new_line.append(curr * 2)
            else:  # prev is not None, but cannot be merged with curr
                if prev != 0:
                    new_line.append(prev)
                prev = curr
        if prev is not None:
            new_line.append(prev)
        # update new board
        new_line.extend([0 for _ in range(N - len(new_line))])  # padding
        for j, val in enumerate(new_line):
            if direction == 'left':
                new_board[i].append(val)
            elif direction == 'right':
                new_board[i].insert(0, val)
            elif direction == 'up':
                new_board[j].append(val)
            else:
                new_board[-(j+1)].append(val)

    return new_board


def get_maximum(board):
    """
    compute maximum value of current board
    """
    return max(max(row) for row in board)


def search(board):
    """
    main search function where backtracking happens
    """
    curr_max = 0
    def backtrack(board, direction, step):
        """
        given initial board state, compute the maximum score one can get in 5 moves
        """
        board = execute_move(board, direction)
        score = get_maximum(board)
        nonlocal curr_max
        # stop exploring if current branch cannot exceed maximum
        if score * 2**(5-step) < curr_max:
            return
        if score > curr_max:
            curr_max = score
        if step < 5:
            for direction in ['left', 'right', 'up', 'down']:
                backtrack(board, direction, step+1)

    # start backtracking
    for direction in ['left', 'right', 'up', 'down']:
        backtrack(board, direction, 1)
    return curr_max

print(search(board))

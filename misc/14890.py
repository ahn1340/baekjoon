N, L = list(map(int, input().split()))
board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)


def is_traversable(board, idx, row):
    """
    from given start position, check if the row or column can be traversed 
    """
    ramps = []  # indices of ramps
    for d in [1, -1]:  # sweep forward and backward
        s = 0 if d == 1 else -1
        if row:
            prev = board[idx][s]
        else:
            prev = board[s][idx]
        counter = 0  # keep track of how many same level grids we had
        for i in range(N)[::d]:
            if row:
                curr = board[idx][i]
            else:
                curr = board[i][idx]
            
            if curr > prev + 1:  # diff is larger than 1
                return False
            elif curr == prev + 1:  # one step up
                if L <= counter:
                    start = min(i - d * 1, i - d * L)
                    end = max(i - d * 1, i - d * L)
                    ramps.append((start, end))
                    prev = curr
                    counter = 1
                else:
                    return False
            elif curr == prev:  # same level
                counter += 1
            else:  # downhill
                prev = curr
                counter = 1

    ramps = sorted(ramps)
    # check if ramps are valid
    for i in range(1, len(ramps)):
        if ramps[i-1][1] >= ramps[i][0]:
            return False
    return True

counter = 0
for row in [True, False]:
    for i in range(N):
        if is_traversable(board, i, row):
            counter += 1

print(counter)

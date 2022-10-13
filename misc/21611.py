def get_marbles_and_dicts(board):
    """
    return:
    1. list of marbles
    2. dict where k: index, v: board position
    3. dict where k: board position, v: inddex
    """
    drs = [0, 1, 0, -1]
    dcs = [-1, 0, 1, 0]
    d = 0  # direction
    steps = 1  # steps for one direction
    r, c = N // 2, N // 2  # position 0
    marbles = [0]
    ind2pos = {}
    pos2ind = {}

    counter = 1
    for i in range(N - 1):
        times = 2 if i < N - 2 else 3
        for _ in range(times):
            for _ in range(steps):
                d %= 4  # direction
                r, c = r + drs[d], c + dcs[d]
                ind2pos[counter] = (r, c)
                pos2ind[(r, c)] = counter
                marbles.append(board[r][c])
                counter += 1
            d += 1
        steps += 1

    return marbles, ind2pos, pos2ind


def remove_marbles(spell, marbles, pos2ind):
    """
    given spell (d, s), remove marbles
    """
    # up, down, left, right
    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]
    d, s = spell[0] - 1, spell[1]
    # get positions of marbles that will be removed
    r, c = N // 2, N // 2  # center
    for i in range(s):
        r, c = r + drs[d], c + dcs[d]
        ind = pos2ind[(r, c)]
        if ind < len(marbles):  # if no marble at given position, then ignore 
            marbles[pos2ind[(r, c)]] = 0  # zero out the removed marbles


def explode(marbles):
    """
    explode marbles and compute score
    """
    scores = [0, 0, 0]
    # convert representation
    mbs = []
    for mb in marbles:
        if mb == 0:  # ignore removed marbles
            continue
        if not mbs:  # empty
            mbs.append([1, mb])
        elif mbs[-1][1] == mb:
            mbs[-1][0] += 1
        else:
            mbs.append([1, mb])

    # explode until done
    exploding = True
    while exploding:
        exploding = False
        new_mbs = []
        for mb in mbs:
            count, num = mb
            if count <= 3:
                # check if this can be merged with previous mb
                if not new_mbs:
                    new_mbs.append(mb)
                elif new_mbs[-1][1] == num:
                    new_mbs[-1][0] += count
                else:
                    new_mbs.append(mb)
            else:
                scores[num-1] += count
                exploding = True
        mbs = new_mbs

    # create new marble list
    marbles = [0]
    for elem in mbs:
        marbles.extend(elem)
        if len(marbles) >= N**2:
            break
    marbles = marbles[:N**2]

    # compute final score
    score = scores[0] + scores[1] * 2 + scores[2] * 3

    
    return marbles, score


#### main part ####
N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

spells = []
for _ in range(M):
    spell = list(map(int, input().split()))
    spells.append(spell)

marbles, ind2pos, pos2ind = get_marbles_and_dicts(board)
total_score = 0
for spell in spells:
    remove_marbles(spell, marbles, pos2ind)
    marbles, score = explode(marbles)
    total_score += score

print(total_score)

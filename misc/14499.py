def roll_die(die, direction):
    """
    Die: [x1, x2, x3, x4, x5, x6], wher 1: top, 2: left, 3: up, 4: right, 5: down, 6: bottom
    direction: one of [1, 2, 3, 4] where 1: right, 2: left, 3: up, 4: down
    permute the numbers given the direction
    """
    new_die = []
    if direction == 1:  # roll rightward
        new_die.extend([die[1], die[5], die[2], die[0], die[4], die[3]])
    elif direction == 2:  # roll leftward
        new_die.extend([die[3], die[0], die[2], die[5], die[4], die[1]])
    elif direction == 3:  # roll upward
        new_die.extend([die[4], die[1], die[0], die[3], die[5], die[2]])
    elif direction == 4:  # roll downward
        new_die.extend([die[2], die[1], die[5], die[3], die[0], die[4]])
        
    return new_die


def roll(world, die, die_pos, direction):
    """
    do one step of update:
    1. roll dice, 2. update numbers, 3. compute new die position
    """
    drs = [0, 0, -1, 1]
    dcs = [1, -1, 0, 0]
    dpr, dpc = die_pos  # die position r and c
    ndpr, ndpc = dpr + drs[direction-1], dpc + dcs[direction-1]  # new die position r and c
    if 0 <= ndpr < N and 0 <= ndpc < M:  # if within map
        # roll die
        die = roll_die(die, direction)
        # if world[ndpr][ndpc] == 0: die -> grid, else: grid -> die
        if world[ndpr][ndpc] == 0:
            world[ndpr][ndpc] = die[5]
        else:
            die[5] = world[ndpr][ndpc]
            world[ndpr][ndpc] = 0
        # new die position
        die_pos = (ndpr, ndpc)

        return die, die_pos, True
    else:
        return die, die_pos, False
        

def simulate(world, die, die_pos, Ks):
    """
    roll die and print for given set of directions
    """
    for direction in Ks:
        die, die_pos, rolled = roll(world, die, die_pos, direction)
        if rolled:
            print(die[0])


##### main funciton #####
# parse input
N, M, x, y, K = list(map(int, input().split()))

world = []
for _ in range(N):
    row = list(map(int, input().split()))
    world.append(row)

# 1: right, 2: left, 3: up, 4: down 
Ks = list(map(int, input().split()))
die_pos = (x, y)
die = [0 for i in range(6)]

simulate(world, die, die_pos, Ks)

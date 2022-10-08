import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

# parse input
world = []

for i in range(N):
    string = sys.stdin.readline()
    string = string[:-1] if string[-1] == '\n' else string
    row = []
    for j, c in enumerate(string):
        if c == '#':
            row.append(1)
        elif c == 'R':
            red = (i, j)
            row.append(0)
        elif c == 'B':
            blue = (i, j)
            row.append(0)
        elif c == 'O':
            row.append(2)  # hole
        else:
            row.append(0)
    world.append(row)
state_init = (red, blue)

def compute_new_pos(world, state, direction, ball='red'):
    # compute where the ball will end up, given state and world
    if direction == 'left':
        move = [0, -1]
    elif direction == 'right':
        move = [0, 1]
    elif direction == 'up':
        move = [-1, 0]
    elif direction == 'down':
        move = [1, 0]
    # determine which ball we are concerned with
    if ball == 'red':
        curr_pos = state[0]
        other_pos = state[1]
    else:
        curr_pos = state[1]
        other_pos = state[0]
    # move the ball until it hits the wall or reaches the hole
    other_on_the_way = False
    hole_reached = False
    while True:
        curr_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
        #print(curr_pos)
        if curr_pos == other_pos:  # other ball is on the way
            other_on_the_way = True
        if world[curr_pos[0]][curr_pos[1]] == 2:  # ball fell into the hole
            hole_reached = True
        if world[curr_pos[0]][curr_pos[1]] == 1:  # ball hit the wall
            curr_pos = (curr_pos[0] - move[0], curr_pos[1] - move[1])
            if other_on_the_way and not hole_reached:  # only go back two steps if hole is not on the path
                curr_pos = (curr_pos[0] - move[0], curr_pos[1] - move[1])
            break
    # return the position where the ball would end up
    return curr_pos, hole_reached
   

def tilt(state, world, direction):
    # tilt the board in the given direction and update state
    new_red_pos, red_in_hole = compute_new_pos(world, state, direction, ball='red')
    new_blue_pos, blue_in_hole = compute_new_pos(world, state, direction, ball='blue')

    return (new_red_pos, new_blue_pos), red_in_hole, blue_in_hole


def bfs(state, world):
    state_dict = {state:True}
    state_queue = deque()
    step_queue = deque()
    state_queue.append(state)
    step_queue.append(0)

    while state_queue:
        state = state_queue.popleft()
        step = step_queue.popleft()
        # get neighbors
        for direction in ['left', 'right', 'up', 'down']:
            new_state, red_in_hole, blue_in_hole = tilt(state, world, direction)
            if not blue_in_hole:
                if red_in_hole:  # termination condition
                    return step + 1
                if step != 9 and new_state not in state_dict:  # add to queue, if step + 1 is less than 10
                    state_dict[new_state] = True
                    state_queue.append(new_state)
                    step_queue.append(step + 1)
    return -1

ans = bfs(state_init, world)
print(ans)

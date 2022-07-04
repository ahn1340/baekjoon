"""
Author: Jin Woo Ahn
백준 1149번 (RGB거리)
"""

n = int(input())
rgb_cost = []
for i in range(n):
    rgb_cost.append(list(map(int, input().split())))

def get_min(rgb_cost, n):
    memo = {0: rgb_cost[0]}
    for i in range(1, n):
        costs = []
        for j in range(3):  # each r g b
            prev_costs = memo[i-1][:]
            prev_costs.pop(j)
            cost = rgb_cost[i][j] + min(prev_costs)
            costs.append(cost)
        memo[i] = costs

    return min(memo[n-1])

print(get_min(rgb_cost, n))

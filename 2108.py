"""
Author: Jin Woo Ahn
백준 2108번 문제 (통계학)
"""

n_nums = int(input())
nums = []
for i in range(n_nums):
    nums.append(int(input()))

nums = sorted(nums)

sum = 0
occur = {}

for num in nums:
    sum += num
    if num not in occur:
        occur[num] = 1
    else:
        occur[num] = occur[num] + 1

# compute mean
mean = round(sum/n_nums)

# compute median
median = nums[n_nums // 2]

# compute mode
sorted_occur = sorted(list(occur.items()), key=lambda x:x[1], reverse=True)
if len(sorted_occur) > 1 and sorted_occur[0][1] == sorted_occur[1][1]:
    mode = sorted_occur[1][0]
else:
    mode = sorted_occur[0][0]

# compute range
range = max(nums) - min(nums)

print(mean)
print(median)
print(mode)
print(range)

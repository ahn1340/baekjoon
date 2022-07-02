"""
Author: Jin Woo Ahn
백준 1620번 (잃어버린 괄호)
"""

# parse input
text = input()
nums = []
ops = ['+']
str = ''
for char in text:
    if char not in ['+', '-']:
        str += char
    else:
        nums.append(str)
        ops.append(char)
        str = ''
nums.append(str)

# solve
def solution(nums, ops):
    # edge case
    if len(nums) == 1:
        return nums[0]
    
    pos = 0
    neg = 0
    is_pos = True
    for i, op in enumerate(ops):
        num = int(nums[i])
        if op == '-':
            is_pos = False
        if is_pos:
            pos += num
        else:
            neg += num
            
    return pos-neg

print(solution(nums,ops))


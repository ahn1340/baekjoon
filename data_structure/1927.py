"""
Author: Jin Woo Ahn
백준 1927번 (min heap)
파이썬을 사용하여 힙 구현 (insertion: O(logn), deletion: O(logn))
"""
import sys

# Heap implementation in Python
def heapify(nums):
    heap = [None]
    for num in nums:
        if num is None:
            pass
        else:
            heap = add(heap, num)
    return heap

def add(heap, num):
    heap.append(num)
    idx = len(heap) - 1
    while idx != 1:
        parent = heap[idx // 2]
        if num < parent:  # swap
            heap[idx // 2] = num
            heap[idx] = parent
            idx //= 2
        else:
            break

def remove_least(heap):
    last = heap[-1]
    least = heap[1]
    heap.pop()  # remove last element
    if len(heap) == 1:  # empty
        return least
    heap[1] = last
    idx = 1
    child = 2
    while True:
    # get the bigger of children
        if child >= len(heap):
            break
        elif child+1 >= len(heap):
            bigger = child
        else:
            bigger = min([child, child+1], key=lambda x: heap[x])
        val = heap[bigger]
        if last > val:
            heap[bigger] = last
            heap[idx] = val
            idx = bigger
            child = bigger * 2
        else:
            break
    return least

N = int(input())
heap = [None]
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 1:
            print('0')
        else:
            least = remove_least(heap)
            print(least)
    else:
        add(heap, num)

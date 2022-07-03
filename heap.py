"""
Author: Jin Woo Ahn
Implementation of min heap from scratch (remove and add)
"""
# min heap
def heapify(nums):
    heap = [None]
    for num in nums:
        if num is None:
            pass
        else:
            add(heap, num)
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
    heap.pop()  # remove last element
    heap[1] = last
    idx = 1
    counter = 0
    while True:
    # get the bigger of children
        idx1, idx2 = idx * 2, idx * 2 + 1
        if idx1 >= len(heap):
            break
        elif idx2 >= len(heap):
            bigger = idx1
        else:
            bigger = min([idx1, idx2], key=lambda x: heap[x])
        val = heap[bigger]
        if last > val:
            heap[bigger] = last
            heap[idx] = val
            idx = bigger
        else:
            break
        counter += 1
        if counter == 20:
            break
 
#import random
#nums = [random.randint(1, 1000) for i in range(20)]
#heap = heapify(nums)

"""
Author: Jin Woo Ahn
백준 17413번 (단어 뒤집기2)
"""

from collections import deque
str = input()

answer = ''
processing_tag = False
queue = deque()
for char in str:
    if char == '<':
        processing_tag = True
        word = ''
        while queue:
            word += queue.pop()
        answer += word
        queue.append(char)
    elif char == '>':
        queue.append(char)
        processing_tag = False
        tag = ''
        while queue:
            tag += queue.popleft()
        answer += tag
    elif char == ' ':
        if processing_tag:
            queue.append(char)
        else:
            word = ''
            while queue:
                word += queue.pop()
            answer += word + ' '
    else:
        queue.append(char)
word = ''
while queue:
    word += queue.pop()
answer += word

print(answer)
        
    

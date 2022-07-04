characters = input()

def solution(str):   
    found_palindrome = False
    for i in range(len(str)):
        # start checking palindrome
        left = i
        right = len(str) - 1
        while not found_palindrome:
            if str[left] != str[right]:
                break
            else:
                left += 1
                right -= 1
                if right - left < 0:
                    found_palindrome = True
        if found_palindrome:
            break

    return len(str) + i
        
print(solution(characters))

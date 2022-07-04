"""
Author: Jin Woo Ahn
baekjoon problem 1254 (팰린드롬 만들기)

"""
characters = list(input())

char_dict = {}
for char in characters:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] = char_dict[char] + 1
        

# at most one character that is not even, otherwise return False
def make_palindrome(char_dict):
    n_odd = 0
    odd_char = ''
    half_dict = {}
    sorted_keys = sorted(char_dict.keys())
    for k in sorted_keys:
        div, rem = divmod(char_dict[k], 2)
        if rem == 1:
            n_odd += 1
            odd_char = k
            half_dict[k] = div
        else:
            half_dict[k] = div
        if n_odd > 1:
            return "I'm Sorry Hansoo"
    
    # generate string
    str = ''
    for k in sorted_keys:
        str += k * half_dict[k]
    reverse = str[::-1]
    answer = str + odd_char + reverse

    return answer

print(make_palindrome(char_dict))

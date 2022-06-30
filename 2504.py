"""
Author: Jin Woo Ahn
problem 2504 (괄호의 합)
"""

str = input()

# start from upper level, go deeper
def compute_paren_val(str):
    if len(str) == 0:
        return 1

    i = 0
    start = i
    stack = []
    parens = []
    while i != len(str):
        if str[i] == '(':
            stack.append(')')
        elif str[i] == '[':
            stack.append(']')
        else:
            if not stack:  # superfluous closing bracket
                return 0
            else:
                char = stack.pop()
                if char != str[i]:  # wrong closing bracket
                    return 0
                else:
                    if not stack:  # found final closing bracket
                        parens.append([start, i])
                        start = i + 1
        i += 1
    # no closing bracket (stack is not empty)
    if stack:
        return 0
    
    # get values of each parens
    paren_val = 0
    for paren in parens:
        start, end = paren[0], paren[1]
        if str[start] == '(':
            factor = 2
        else:
            factor = 3
            
        substr = str[start+1:end]
        #print(f"processing substring: {substr}")
        substr_val = compute_paren_val(substr) * factor  #recursion
        #print(f"substr_val: {substr_val}")
        paren_val += substr_val

    return paren_val
    

print(compute_paren_val(str))

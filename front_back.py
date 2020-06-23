# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    first_char = str[0]
    last_char = str[-1]
    return last_char + str[1:-1] + first_char 


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
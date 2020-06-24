# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    return n * str


# Solution 2
def string_times2(str, n):
    result = "" #empty string 
    
    for i in range(n):
        result = result + str
    return result

print(string_times('Hi', 2)) # 'HiHi'

print(string_times('Hi', 3)) # 'HiHiHi'

print(string_times('Hi', 1)) # 'Hi')


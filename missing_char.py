# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    return str.replace(str[n], "")


# solution 2

def missing_char2(str, n):
    front_str = [:n] # up to but not including index n
    back_str = [n+1:] # from n+1 to the end of the string
    return front_str + back_str
    
print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))


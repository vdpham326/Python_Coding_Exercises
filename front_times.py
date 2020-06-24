# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or 
# whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
    if len(str) < 3:
        return str * n
    return str[:3] * n


def front_times2(str, n):
    result = "" # empty string 
    if len(str) < 3:
        for i in range(n):
            result += str

    for i in range(n):
        result += str[:3]
    return result


print(front_times('Chocolate', 2)) # 'ChoCho
print(front_times2('Chocolate', 3)) # ChoChoCho
print(front_times2('Abc', 3))



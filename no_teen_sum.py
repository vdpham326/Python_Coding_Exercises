
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not 
# count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen 
# code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# def no_teen_sum(a, b, c):
#     sum = 0
#     if a in range(13, 20):
#         if a == 15 or a == 16:
#             sum += a
#         a = 0
#     if b in range(13, 20):
#         if b in range(15, 17):
#             sum += b
#         b = 0
#     if c in range(13, 20):
#         if c in range(15, 17):
#             sum += c
#         c = 0
#     else:
#         sum = a + b + c
#     return sum


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n > 12 and n < 20 and not n == 15 and not n == 16:
        return 0
    else:
        return n
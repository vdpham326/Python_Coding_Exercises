
# Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


def sum3b(nums):
    return sum(nums)

print(sum3([1, 2, 3]))
print(sum3b([5, 11, 2]))
print(sum3([7, 0, 0])) 


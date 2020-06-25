
# Given an array of ints length 3, figure out which is larger, 
# the first or last element in the array, and set all the other elements to be that value. Return the changed array.


def max_end3(nums):
    new = []
    if nums[0] > nums[-1]:
        for i in range(len(nums)):
            new.append(nums[0])
    elif nums[0] < nums[-1]:
         for i in range(len(nums)):
            new.append(nums[-1])
    else:
         for i in range(len(nums)):
            new.append(nums[0])
    return new



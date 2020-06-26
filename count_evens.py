def count_evens(nums):
    '''
    Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    '''
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
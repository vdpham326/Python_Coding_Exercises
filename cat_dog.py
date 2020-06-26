def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat = 0
    dog = 0

    for i in range(len(str)):
        if str[i: i + 3] == 'cat':
            cat += 1
    
    for i in range(len(str)):
        if str[i: i + 3] == 'dog':
            dog += 1
    return cat == dog
        


#Solution 2
def cat_dog2(str):
    return str.count('cat') == str.count('dog')
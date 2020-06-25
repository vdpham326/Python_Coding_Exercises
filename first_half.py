# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    half = int(len(str) / 2)
    return str[:half]
    #return half

print(first_half('Woohoo'))
print(first_half('HelloThere'))
print(first_half('abcdefg'))

#print(first_half('Woohoo'))

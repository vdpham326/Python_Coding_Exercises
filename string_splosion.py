# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    new_str = ""
    for i in range(len(str)):
        new_str = new_str + str[:i+1]
    return new_str

print(string_splosion('Code'))
print(string_splosion('abc'))
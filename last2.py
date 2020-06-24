# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the 
# string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    # if string length less than 2
    # if len(str) < 2:
    #     return 0
  count = 0
  for i in range(0, len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count

print(last2('axxxaaxx'))


    
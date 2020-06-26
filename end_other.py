def end_other(a, b):
    '''
    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences 
    (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
    '''

    # print(-len(b))
    # #print(a[-3:])
    # print(a[-len(b):].lower())
    if len(a) == len(b):
        if a.lower() == b.lower(): return True
    elif len(a) > len(b): # check if string b is at the end of string a
        if b.lower() == a[-len(b):].lower():
            return True
    elif len(a) < len(b):
        if a.lower() == b[-len(a):].lower():
            return True
    return False



#solution 2

def end_other(a, b):
  """
  Given two strings, return True if either of the strings appears at the very 
  end of the other string, ignoring upper/lower case differences (in other 
  words, the computation should not be "case sensitive").
  """
  long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
  return long_s.lower().endswith(short_s.lower())

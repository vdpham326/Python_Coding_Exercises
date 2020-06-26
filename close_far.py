
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from 
# both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  abs_b = abs(b-a)
  abs_c = abs(c-a)
  abs_c2 = abs(c-b)
  if abs_b <=1:
    return abs_c >=2 and abs_c2 >=2
  elif abs_c <=1:
    return abs_b >=2 and abs_c2 >=2
  else:
    return False
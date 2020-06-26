
# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


def in1to10(n, outside_mode):
    if outside_mode and (n <= 1 or n >= 10):
      return True
    elif outside_mode and not (n <= 1 or n >= 10):
      return False
    return (n >= 1 and n <= 10)



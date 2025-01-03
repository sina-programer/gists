# if condition a**2 == b**2 + c**2 holds for any combination of sides the triangle will be a right-angle

def is_right_angle_efficient(a, b, c):
  mx = max(a, b, c)
  return mx**2 == a**2 + b**2 + c**2 - mx**2

def is_right_angle_ordinary(a, b, c):
  if a**2 == b**2 + c**2:
    return True
  elif b**2 == a**2 + c**2:
    return True
  elif c**2 == a**2 + b**2:
    return True
  return False


if __name__ == '__main__':
  test_cases = [
    [3, 4, 5],  # True
    [6, 8, 10],  # True
    [1, 2, 3],  # False
    [6, 7, 8]  # False
  ]
  
  # as we sure ordinary method works well, we check new efficient way results be the same as ordinary ones
  print(all(map(lambda case: is_right_angle_efficient(*case) == is_right_angle_ordinary(*case), test_cases)))

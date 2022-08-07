#  --- Directions
#  Write a function that accepts a positive number N.
#  The function should console log a pyramid shape
#  with N levels using the # character.  Make sure the
#  pyramid has spaces on both the left *and* right hand sides
#  --- Examples
#  pyramid(1)
#  '#'
#  pyramid(2)
#  ' # '
#  '###'
#  pyramid(3)
#  '  #  '
#  ' ### '
#  '#####'

import math

def pyramid(n, row=0, level=' '):
    if n == 0:
      print("#")
    for step in range(1, n + 1):
        print(f"{level}" * (n - step) + "#" * ( 2 * step - 1) + f"{level}" * (n - step))


# def pyramid(n, row=0, level=' '):
#     midpoint = math.floor((2 * n - 1) / 2)
#     for row in range(n):
#       level = ""
#       for column in range(n * 2 - 1):
#         if midpoint - row <= column and midpoint + row >= column:
#           level += "#"
#         else:
#           level += " "
#       print(level)

# def pyramid(n, row=0, level=''):
#     if n == row:
#       return

#     if 2 * n - 1 == len(level):
#       print(level)
#       return pyramid(n, row +  1)

#     midpoint = math.floor((2 * n - 1) / 2)
#     if midpoint - row <= len(level) and midpoint + row >= len(level):
#       add = "#"
#     else:
#       add = " "

#     pyramid(n, row, level + add)

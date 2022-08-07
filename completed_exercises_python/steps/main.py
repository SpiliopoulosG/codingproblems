#  --- Directions
#  Write a function that accepts a positive number N.
#  The function should console log a step shape
#  with N levels using the # character.  Make sure the
#  step has spaces on the right hand side!
#  --- Examples
#  steps(2)
#  '# '
#  '##'
#  steps(3)
#  '#  '
#  '## '
#  '###'
#  steps(4)
#  '#   '
#  '##  '
#  '### '
#  '####'

def steps(n, row = 0, stair = ' '):
    if n == 0:
      print("#")
    for step in range(1, n + 1):
        print("#" * step + f"{stair}" * (n - step))
  

# def steps(n, row = 0, stair = ' '):
#   for row in range(n):
#     stair = ""
#     for column in range(n):
#       if column <= row:
#         stair += "#"
#       else:
#         stair += " "
#     print(stair)

# def steps(n, row = 0, stair = ''):
#   if n == row:
#     return 

#   if n == len(stair):
#     print(stair)
#     return steps(n, row +  1)

#   if len(stair) <= row:
#     stair += "#"
#   else:
#     stair += " "
  
#   steps(n, row, stair)
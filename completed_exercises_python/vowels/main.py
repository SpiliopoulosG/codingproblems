#  --- Directions
#  Write a function that returns the number of vowels
#  used in a string.  Vowels are the characters 'a', 'e'
#  'i', 'o', and 'u'.
#  --- Examples
#  vowels('Hi There!') --> 3
#  vowels('Why do you ask?') --> 4
#  vowels('Why?') --> 0

def vowels(str):
  sum = 0
  vowels = ["a", "e", "i", "o", "u"]
  for letter in str:
    if letter.lower() in vowels:
      sum += 1
  return sum

# def vowels(str):
#   sum = 0 
#   for letter in str:
#     char = letter.lower()
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#       sum += 1
#   return sum



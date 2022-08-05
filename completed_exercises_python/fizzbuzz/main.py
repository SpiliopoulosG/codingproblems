#  --- Directions
#  Return a number from 1 to n. But for multiples of three return
#  “Fizz” instead of the number and for the multiples
#  of five return “Buzz”. For numbers which are multiples
#  of both three and five return “FizzBuzz”.
#  --- Example
#  fizzBuzz(5)
#  buzz

def fizzBuzz(num):
    endword = ""
    if num % 3 == 0:
        endword += "Fizz"
    if num % 5 == 0:
        endword += "Buzz"
    if endword != "":
        return endword
    else:
        return num

# def fizzBuzz(num):
#     if num % 15 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     else:
#         return num

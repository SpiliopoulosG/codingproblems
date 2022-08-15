import math

def find_factorial_iterative(number):
    answer = 1
    for i in range(2, number + 1):
        answer = answer * i

    return answer


def find_factorial_recursive(number):
    if number == 1:
        return 1
    return number * find_factorial_recursive(number - 1)



# Implement a function that reverses a string using iteration... and then recursion!
# def reverse_string(str):
#     letters_list = []
#     end_string = ""

#     for index in range(len(str)):
#         letters_list.append(str[index])

#     for index in range(len(letters_list)):
#         end_string += letters_list.pop()

#     return end_string


def reverse_string(str):
    
    

print(reverse_string('yoyo mastery'))
# should return: 'yretsam oyoy'

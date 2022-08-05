# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do * include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
# palindrome("abba") == = true
# palindrome("abcdefg") == = false

import math

def palindrome(str):
    character_list = []
    for i in range(len(str)):
        character_list.append(str[len(str) - 1 - i])
    for index in range(math.ceil(len(character_list)/2)):
        if character_list[index] != character_list[len(character_list) - 1 - index]:
            return False
    return True

# def palindrome(str):
#     for i in range(len(str)):
#         print(str[i], str[len(str) - 1 - i])
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     return True

# def palindrome(str):
#     return "".join([str[(len(str) - 1 - index)] for index in range(len(str))]) == str

# def palindrome(str):
#     reversed = ""
#     for character in str:
#         reversed = character + reversed
#     return reversed == str

# def palindrome(str):
#     return "".join(reversed(str)) == str

# def palindrome(str):
#     return str[::-1 ]== str

#  --- Directions
#  Given a string, return the character that is most
#  commonly used in the string.
#  --- Examples
#  maxChar("abcccccccd") === "c"
#  maxChar("apple 1231111") === "1"

def maxChar(str):
    char_dict = {}
    for char in str:
        if char_dict.get(char) is not None:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1

    highest_value = 0
    highest_value_char = 0
    for key, value in char_dict.items():
        if value > highest_value:
            highest_value = value
            highest_value_char = key
    return highest_value_char

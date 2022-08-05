
# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
# reverse('apple') == = 'leppa'
# reverse('hello') == = 'olleh'
# reverse('Greetings!') == = '!sgniteerG'

def reverse(str):
    character_list = []
    for i in range(len(str)):
        character_list.append(str[len(str) - 1 - i])
    return "".join(character_list)

# def reverse(str):
#     return str[::-1]

# def reverse(str):
#     return "".join(reversed(str))

# def reverse(str):
#     reversed = ""
#     for character in str:
#         reversed = character + reversed
#     return reversed


# def reverse(str):
#     return "".join([str[(len(str) - 1 - index)] for index in range(len(str))])



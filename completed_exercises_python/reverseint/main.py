#  --- Directions
#  Given an integer, return an integer that is the reverse
#  ordering of numbers.
#  --- Examples
#    reverseInt(15) === 51
#    reverseInt(981) === 189
#    reverseInt(500) === 5
#    reverseInt(-15) === -51
#    reverseInt(-90) === -9

def reverseInt(n):
    needs_minus = False
    if str(n) == '0':
        return n
    if str(n)[0] == '-':
        needs_minus = True
    if needs_minus:
        return int("-" + str(n)[::-1].lstrip("0").strip("-"))
    return int(str(n)[::-1].lstrip("0").strip("-"))

# def reverseInt(n):
#     needs_minus = False
#     if str(n) == '0':
#         return n
#     if str(n)[0] == '-':
#         needs_minus = True
#     if needs_minus:
#         return int("-" + ("".join(reversed(str(n))).lstrip("0").strip("-")))
#     return int(("".join(reversed(str(n))).lstrip("0").strip("-")))


# def reverseInt(n):
#     needs_minus = False
#     if str(n) == '0':
#         return n
#     if str(n)[0] == '-':
#         needs_minus = True
#     reversed = ""
#     for character in str(n):
#         reversed = character + reversed
#     if needs_minus:
#         return int("-" + reversed.lstrip("0").rstrip("-"))
#     return int(reversed.lstrip("0").rstrip("-"))

#  --- Directions
#  Check to see if two provided strings are anagrams of eachother.
#  One string is an anagram of another if it uses the same characters
#  in the same quantity. Only consider characters, not spaces
#  or punctuation.  Consider capital letters to be the same as lower case
#  --- Examples
#  anagrams('rail safety', 'fairy tales') --> True
#  anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#  anagrams('Hi there', 'Bye there') --> False

def anagrams(stringA, stringB):
    first_word_dict = cleanString(stringA)
    second_word_dict = cleanString(stringB)

    if len(first_word_dict) != len(second_word_dict):
      return False
    else:
      for key, value in first_word_dict.items():
        if first_word_dict.get(key) != second_word_dict[key]:
          return False
      return True


def cleanString(string):
    list_to_return = []
    sentence = string.split()

    for word in sentence:
      list_to_return.append(word.strip("!").lower())
      
    final_word = ''.join(list_to_return)
    word_dict = {}
    for letter in final_word:
        if word_dict.get(letter) == None:
          word_dict[letter] = 1
        else:
          word_dict[letter] += 1
    return word_dict

# def anagrams(stringA, stringB):
#     first_word_sorted = cleanString(stringA)
#     second_word_sorted = cleanString(stringB)
    
#     if first_word_sorted != second_word_sorted:
#       return False
#     return True

# def cleanString(string):
#     unsorted_word = ""
#     sentence = string.split()
#     for word in sentence:
#       word = word.strip("!").lower()
#       unsorted_word += word
#     return "".join(sorted(unsorted_word))


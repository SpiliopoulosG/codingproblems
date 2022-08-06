#  --- Directions
#  Write a function that accepts a string.  The function should
#  capitalize the first letter of each word in the string then
#  return the capitalized string.
#  --- Examples
#  capitalize('a short sentence') --> 'A Short Sentence'
#  capitalize('a lazy fox') --> 'A Lazy Fox'
#  capitalize('look, it is working!') --> 'Look, It Is Working!'


def capitalize(str):
    list = str.split()
    end_list = []
    for word in list:
      end_list.append(word.capitalize())
    return " ".join(end_list)

    
 

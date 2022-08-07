
def firstRecurringChar(numlist):
    if not isinstance(numlist, list):
        return ["Not a list"]

    number_dictionary = {}
    for index in range(len(numlist)):
        # print(numlist[index])
        
        if number_dictionary.get(numlist[index]) != None:
                return numlist[index]

        if number_dictionary.get(numlist[index]) == None:
            number_dictionary[numlist[index]] = 1


    return None

print(firstRecurringChar(numlist = [2,5,1,2,3,5,1,2,4]))  
print(firstRecurringChar(numlist = [2,1,1,2,3,5,1,2,4]))
print(firstRecurringChar(numlist = [2,3,4,5]))
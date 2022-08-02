
def sumtwo(numlist, target):
    if not isinstance(numlist, list):
        return ["Not a list"]

    if not isinstance(target, int):
        return ["Not a valid target"]


    remaining_dictionary = {}
    for index in range(len(numlist)):
        # print(numlist[index])
        if numlist[index] == target:
            print("\n")
            return index

        if remaining_dictionary.get(numlist[index]) != None:
            return [remaining_dictionary.get(numlist[index]), index]

        remaining_dictionary[target - numlist[index]] = index


    print(remaining_dictionary)

print(sumtwo(numlist = [3,3], target = 6))
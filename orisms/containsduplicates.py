def containsDuplicate(nums):
    if not isinstance(nums, list):
        return ["Not a list"]

    number_dictionary = {}
    for index in range(len(nums)):

        if number_dictionary.get(nums[index]) != None:
            return True

        if number_dictionary.get(nums[index]) == None:
            number_dictionary[nums[index]] = 1

    return False


print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
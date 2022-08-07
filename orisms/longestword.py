def longestWord(string):
    word_list = []
    word_list = string.split(' ')

    highest_number_index = 0
    for index in range(len(word_list)):
        if len(word_list[index]) > len(word_list[highest_number_index]):
            highest_number_index = index

    return word_list[highest_number_index] 

print(longestWord("I love dogs"))
print(longestWord("fun &!! time"))

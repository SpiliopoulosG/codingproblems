#  --- Directions
#  Given an array and chunk size, divide the array into many subarrays
#  where each subarray is of length size
#  --- Examples
#  chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
#  chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
#  chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
#  chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
#  chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

import math

def chunk(array, size):
    chunked_list = list()
    for i in range(0, len(array), size):
        chunked_list.append(array[i:i+size])
    return chunked_list

# def chunk(array, size):
#   chunked = []
#   index = 0
#   while index < len(array):
#       chunked.append(array[slice(index, index + size)])
#       index += size
#   return chunked

# def chunk(array, size):
#     final_list = []
#     for index in range(math.ceil(len(array)/size)):
#       chunk = []
#       for i in range(size):
#         if len(array) != 0:
#           chunk.append(array.pop(0))
#       final_list.append(chunk)

#     return final_list



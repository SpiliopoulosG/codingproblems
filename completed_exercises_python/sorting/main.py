#  --- Directions
#  Implement bubble_sort, selection_sort, and merge_sort
import math

def bubble_sort(arr):
    
    for index in range(0, len(arr)):
        for j in range(0, (len(arr) - index - 1)):
            if arr[j] > arr[j + 1]:
                temporary = arr[j]
                arr[j] = arr[j +  1]
                arr[j + 1] = temporary

    return arr

def selection_sort(arr):

    for index in range(0, len(arr)):
        index_of_minimum = index
        for j in range(index + 1, (len(arr))):
            if arr[index_of_minimum] > arr[j]:
                index_of_minimum = j

        if index != index_of_minimum:
          temporary = arr[index]
          arr[index] = arr[index_of_minimum]
          arr[index_of_minimum] = temporary

    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    center = math.floor(len(arr) / 2)
    left = arr[0:center]
    right = arr[center:]

    
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):

    results = []
  
    while len(left) != 0 and len(right) != 0:

        if left[0] > right[0]:
            results.append(right.pop(0))
        else: 
            results.append(left.pop(0))

    if len(right) != 0:
        for item in right:
            results.append(item)

    if len(left) != 0:
        for item in left:
            results.append(item)

    return results
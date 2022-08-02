from shutil import move


def moveZeroes(nums):
    if not isinstance(nums, list):
        return ["Not a list"]


    list_without_zeroes = [num for num in nums if num != 0 ]
    list_of_zeroes = [num for num in nums if num == 0 ] 
    
    list_without_zeroes.extend(list_of_zeroes)
    
    final_list = list_without_zeroes
    
    return final_list

print(moveZeroes([0,1,0,3,12]))
def rotate(nums, k):
    if not isinstance(nums, list):
        return ["Not a list"]

    if not isinstance(k, int):
        return ["Not a valid steps"]

    if k > len(nums):
        k = k % len(nums)

    final_list = []
    list_to_insert = []
    for i in range(k):
        list_to_insert.append(nums.pop())

    final_list.extend(list_to_insert[::-1])
    final_list.extend(nums)
    
    return final_list
    
    


print(rotate(nums=[1,2,3,4,5,6,7], k=43))
print(rotate(nums=[-1,-100,3,99], k=2))
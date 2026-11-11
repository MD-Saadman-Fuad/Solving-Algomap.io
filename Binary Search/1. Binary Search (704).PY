def binary_search(nums, target):

    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums)-1
    

    while low <= high : 
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid -1
        else: 
            low = mid + 1


    return -1

nums_1 = [-1,0,3,5,9,12]
target_1 = 9
nums_2 = [-1,0,3,5,9,12]
target_2 = 2
print(binary_search(nums_1, target_1))
print(binary_search(nums_2, target_2))
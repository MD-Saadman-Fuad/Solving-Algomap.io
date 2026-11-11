def searchInsert ( nums, target):

    low = 0
    high = len(nums)-1
    while low <=high:
        mid = (low+high) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return low

nums_1 = [1, 3, 5, 6]
target_1 = 5

nums_2 = [1, 3, 5, 6]
target_2 = 2

nums_3 = [1, 3, 5, 6]
target_3 = 7

print(searchInsert(nums_1, target_1))  # 2
print(searchInsert(nums_2, target_2))  # 1
print(searchInsert(nums_3, target_3))  # 4
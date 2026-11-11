
def findMin(nums):

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2

        if nums[mid]>nu            

# --- TEST CASES ---

nums_1 = [3, 4, 5, 1, 2]

nums_2 = [4, 5, 6, 7, 0, 1, 2]

nums_3 = [11, 13, 15, 17]

nums_4 = [2, 1]

nums_5 = [1]


# --- OUTPUT ---

print(findMin(nums_1))  # Expected: 1
print(findMin(nums_2))  # Expected: 0
print(findMin(nums_3))  # Expected: 11
print(findMin(nums_4))  # Expected: 1
print(findMin(nums_5))  # Expected: 1

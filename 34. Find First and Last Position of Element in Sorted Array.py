class Solution:
    def searchRange(self, nums, target):
        # left =  0 
        # right = len(nums) - 1
        # result = [-1, -1]
        # for num in range(len(nums)):

        #     if nums[left] == target and result[0] == -1:
        #         result[0] = left
        #     if nums[right] == target and result[1] == -1:
        #         result[1] = right

        #     left += 1
        #     right -= 1
        # return result

        def binarysearch(nums, target, flag):
            left, right = 0, len(nums) - 1
            result = -1

            while left <=right :
                mid = left + right-left // 2

                if nums[mid] == target:
                    if flag:
                        right = mid - 1
                    else:
                        left = mid + 1
                    result = mid
                elif nums[mid] <target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return [binarysearch(nums, target, True), binarysearch(nums, target, False)]

x = Solution()

print(x.searchRange([5,7,7,8,8,10], 8))

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
print(x.searchRange([5,7,7,8,8,10], 6))
print(x.searchRange([], 0))
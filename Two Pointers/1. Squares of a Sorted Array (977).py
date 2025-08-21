class Solution:
    def sortedSquares(self, nums):
        # solve 1
        # abs_value = []

        # for num in nums:
        #     abs_value.append(abs(num))
        # abs_value = sorted(abs_value)
        # # return abs_value

        # for i in range(len(nums)):
        #     abs_value[i] = abs_value[i] ** 2
        # return abs_value

        # solve 2
        # for num in range(len(nums)):
        #     nums[num] = nums[num] ** 2
        # return sorted(nums)
        

        # Optimal O(n)
        # Two pointer approach

        left = 0
        right = len(nums)-1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        result.reverse()
        return result




x = Solution()
nums = [-4,-1,0,3,10]
print(x.sortedSquares(nums))
nums = [-7,-3,2,3,11]
print(x.sortedSquares(nums))


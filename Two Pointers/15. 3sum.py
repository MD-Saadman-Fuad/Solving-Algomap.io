class Solution:
    def threeSum(self, nums):
        
        result = []
        # nums = [-1,0,1,2,-1,-4]
        for first in range(len(nums)-2):
            remain = -nums[first]
            left = first + 1
            right = len(nums) - 1
            print(left , right, first, remain)
            while left < right:
                if nums[left] + nums[right] == remain:
                    print('found')
                    # print(remain, nums[first], nums[left], nums[right])
                    triplet = [nums[first], nums[left], nums[right]]
                    if triplet not in result:
                        result.append(triplet)
                left+=1
                right-=1
            # return result
        
        # # Brute Force
        # result = []
        # for first in range(len(nums)-2):
        #     f = nums[first]
        #     for second in range(first+1, len(nums)-1):
        #         s = nums[second]
        #         for third in range(second+1, len(nums)):
        #             t = nums[third]
        #             if f + s + t == 0:
        #                 if sorted([f,s,t]) not in result:
        #                     result.append(sorted([f,s,t]))
        # return result
            



x  = Solution()
nums = [-1,0,1,2,-1,-4]
print(x.threeSum(nums))
nums = [0,1,1]
# print(x.threeSum(nums))

nums = [0,0,0]
# print(x.threeSum(nums))

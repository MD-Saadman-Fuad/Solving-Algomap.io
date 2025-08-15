class Solution:
    def longestConsecutive(self, nums):
        occurance = set()

        for num in nums:
            if num not in occurance:
                occurance.add(num)
        occurance = sorted(occurance)
        # to be continued

x = Solution()
nums = [100,4,200,1,3,2]
print(x.longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(x.longestConsecutive(nums))
nums = [1,0,1,2]
print(x.longestConsecutive(nums))
class Solution:
    def twoSum(self, nums, target):
        map_nums = {}

        for i in range(len(nums)):
            num_2  = target - nums[i]
            if num_2 in map_nums:
                return [map_nums[num_2], i]
            map_nums[nums[i]] = i
        return []

x=Solution()
print(x.twoSum(nums = [2,7,11,15], target = 9))
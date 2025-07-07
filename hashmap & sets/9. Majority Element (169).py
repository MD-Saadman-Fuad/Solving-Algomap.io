class Solution:
    def majorityElement(self, nums):
        # from collections import Counter
        # length = len(nums)

        # numDict  = Counter(nums)

        # for key in numDict:
        #     if numDict[key] >= length/2:
        #         return key

        map_nums = {}
        length  = len(nums)

        for num in nums:
            if num in map_nums:
                map_nums[num] += 1
            else:
                map_nums[num] = 1
        # print(map_nums)
        
        for map_num in map_nums:
            if map_nums[map_num] >= length / 2:
                return map_num

            





nums  = [2,2,1,1,1,2,2]

x = Solution()

print(x.majorityElement(nums))
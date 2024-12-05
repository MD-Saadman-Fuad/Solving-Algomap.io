class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
#brute force O(n*2)
        # adding = []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

#O(n) using set 
        # store = set()

        # for num in nums:
        #     if num in store:
        #         return True
        #     else:
        #         store.add(num)
        # return False


#O(n) using counter
        # from collections import Counter
        # count_dict = Counter(nums)
        # for value in count_dict.values():
        #     if value > 1:
        #         return True
        # return False

#Best one I got (logical)

        return len(set(nums)) != len(nums)
    
s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
nums=[1]
print(s.containsDuplicate(nums))
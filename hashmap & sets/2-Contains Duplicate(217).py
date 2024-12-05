class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        from collections import Counter
        count_dict = Counter(nums)
        for value in count_dict.values():
            if value > 1:
                return True
        return False
    
s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
nums=[1]
print(s.containsDuplicate(nums))
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        numset = {}

        for num in nums:
            if num in numset:
                numset[num] +=1
            else:
                numset[num] =1
        
        for i in range(len(nums)):

            if 0 in numset and numset[0]>0:
                nums[i] = 0
                numset[0] = numset[0]-1
            elif 1 in numset and numset[1]>0:
                nums[i] = 1
                numset[1] = numset[1]-1
            elif 2 in numset and numset[2]>0:
                nums[i] = 2
                numset[2] = numset[2] -1
        return nums

        
        



x= Solution()
print(x.sortColors([2,0,2,1,1,0]))
print(x.sortColors([2,0,1]))
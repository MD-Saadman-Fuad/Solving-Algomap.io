class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
#initial logic
        # answer = None
        # num = 0
        # for i in range(len(nums)):
        #     j = nums[i]
        #     if j < 0:
        #         j=j*(-1)
        #     distance = j
        #     if answer == None:
        #         answer = distance
        #         num = nums[i]
        #     else:
        #         if distance < answer:
        #             answer = distance
        #             num = nums[i]
        #         elif distance == answer:
        #             if nums[i] > num:
        #                 num = nums[i]
#optimal solution O(n)
        answer = nums[0]
        for i in nums:
            if abs(i) < abs(answer):
                answer = i
        if answer < 0 and abs(answer) in nums:
            answer =  abs(answer)
        return answer

        return num
s = Solution()
nums = [2,-1,1]
print(s.findClosestNumber(nums))
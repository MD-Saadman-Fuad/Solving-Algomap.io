class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        
#Brute force approach
# 
        
        # answer = []

        # for i in range(len(nums)):
        #     store = 1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             store = store * nums[j]
        #     answer.append(store)
        # return answer

#O(n) approach

            n = len(nums)
            left = 1
            right = 1
            left_part = [0] * n
            right_part = [0] * n
            answer = [0] * n

            for i in range(n):
                j = -i-1

                left_part[i] = left
                left = left * nums[i]

                right_part[j] = right
                right = right * nums[j]

            for x in range(n):
                answer[x] = left_part[x] * right_part[x]
            return answer            

s = Solution()
print(s.productExceptSelf([1,2,3,4]))

class Solution:
    def twoSum(self, numbers, target):
        # brute force
        length = len(numbers)

        # for number in range(length):
        #     store = numbers[number]
        #     for j in range(number+1, length):
        #         if target == numbers[number] + numbers[j]:
        #             return [number+1, j+1]

        # Correct answer

        l=0
        r=length-1

        while l<r:
            if target == numbers[l] + numbers[r]:
                return [l+1, r+1]
            
            if target > numbers[l] + numbers[r]:
                l+=1
            if target < numbers[l] + numbers[r]:
                r-=1
            





x=Solution()
numbers = [2,7,11,15]
target = 9
print(x.twoSum(numbers, target))
numbers = [2,3,4]
target = 6
print(x.twoSum(numbers, target))
numbers = [-1,0]
target = -1
print(x.twoSum(numbers, target))

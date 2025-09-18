class Solution:
    def plusOne(self, digits):

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

        # Not optimal, cant do string conversion
        # number = ''
        # length = len(digits) - 1 
        # for digit in digits:
        #     number = number + str(digit)
        # number = int(number) + 1
        # print(type(number))

        # result = []

        # number = str(number)
        # for num in number:
        #     result.append(int(num))
        # # print(result)
        # return result
        

x  = Solution()
print(x.plusOne([1,2,3]))
print(x.plusOne([4,3,2,1]))
print(x.plusOne([9]))
print(x.plusOne([9,9,9]))
print(x.plusOne([0]))
print(x.plusOne([1,2,9]))
print(x.plusOne([1,9,9]))
print(x.plusOne([2,9,9]))
print(x.plusOne([9,8,7,6,5,4,3,2,1,0]))
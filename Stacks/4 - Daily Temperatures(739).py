class Solution:
    def dailyTemperatures(self, temperatures):
      #this excceeded time limit
      length = len(temperatures) 
      stack = [0] * length

      for i in range(length):
        j = i+1
        while j < length and  temperatures[i] >= temperatures[j]  :
          # stack[i] = stack[i]+1
          j+=1
        if j < length:
          stack[i] = j-i
      return stack
      print(stack) 

x = Solution()
temperatures = [73,74,75,71,69,72,76,73] #[1,1,4,2,1,1,0,0]
x.dailyTemperatures(temperatures)
class Solution:
    def isValid(self, s):

        stack = [] 

        if len(s) % 2 != 0:
          return False
        

        for i in s:
          if stack == []:
            return False
          if i in '({[':
            stack.append(i)
          else:
            if i == ')' and stack[-1] == '(':
              stack.pop()
            elif i == '}' and stack[-1] == '{':
              stack.pop()
            elif i == ']' and stack[-1] == '[':
              stack.pop()
            else:
              return False
        if len(stack) > 0:
          return False 
        return True  



x = Solution()
s = "()"
print(x.isValid(s)) # True
s = "()[]{}"
print(x.isValid(s)) # True
s = "(]"
print(x.isValid(s)) # False
s= "([])"
print(x.isValid(s)) # True
s= "()[]{}"
print(x.isValid(s)) # True

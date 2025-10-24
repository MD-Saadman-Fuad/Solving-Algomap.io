class Solution:
    def evalRPN(self, tokens):
        stack = []
        

        if tokens == []:
          return 0
        
        for i in tokens:
        #   print(stack, i)
          if i == '+':
            new = stack.pop()+stack.pop()
            stack.append(new)
          elif i == '-':
            f = stack.pop()
            s = stack.pop()
            new = s - f
            stack.append(new)
          elif i == "*":
            f = stack.pop()
            s = stack.pop()
            new = s * f
            stack.append(new)
          elif i == '/':
            f = stack.pop()
            s = stack.pop()
            new = s / f
            stack.append(int(new))
          else:
            stack.append(int(i))
        return stack[0]




x = Solution()
tokens = ["2","1","+","3","*"]
print(x.evalRPN(tokens)) # 9
tokens = ["4","13","5","/","+"]
print(x.evalRPN(tokens)) # 6
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(x.evalRPN(tokens)) # 22
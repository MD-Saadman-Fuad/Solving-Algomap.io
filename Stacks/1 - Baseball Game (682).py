class Solution:
    def calPoints(self, operations):

        score = []
        sum = 0

        for i in range(len(operations)):
            if operations[i] == '+':
               new_score  = score[len(score)-2] + score[len(score)-1]
               score.append(new_score)
            elif operations[i] == "D":
                new_score = score[len(score)-1] * 2
                score.append(new_score)
            elif operations[i] == "C":
                score.pop()
            else:
                score.append(int(operations[i]))
        
        for j in range(len(score)):
            sum = sum + score[j]
        return sum
        
x = Solution()
operations = ["5","2","C","D","+"]
print(x.calPoints(operations))
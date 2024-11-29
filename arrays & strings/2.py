class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = ""

        if len(word1) <= len(word2):
            X = len(word1)
        else:
            X = len(word2)

        for i in range(X):
            answer+=word1[i]+word2[i]

        if len(word1)> len(word2):
            answer += word1[len(word2):]

        elif len(word1) < len(word2):
            answer += word2[len(word1):]

        else:
            pass
        
        return answer
    

s=Solution()
word1 = "abc"
word2 = "pqr"
print(s.mergeAlternately(word1, word2))
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        answer = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                answer -= m[s[i]]
            else:
                answer += m[s[i]]

        # i = 0
        # while i< len(s):
        #     if i < (len(s)-1) and m[s[i]] < m[s[i+1]]:
        #         answer += m[s[i+1]] - m[s[i]]
        #         i+=2
        #     else:
        #         answer += m[s[i]]
        #         i+=1
        
        return answer
        
    
s=Solution()
str1 = "MCMXCIV"
print(s.romanToInt(str1))
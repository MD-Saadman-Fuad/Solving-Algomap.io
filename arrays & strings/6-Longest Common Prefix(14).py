class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        strs = sorted(strs)

        word1 = strs[0]
        word2 = strs[-1]
        

        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                answer += word1[i]
            else:
                break
        return answer
    
s=Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
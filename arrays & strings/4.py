class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new_len = len(s)
        original_len = len(t)
        
        if s == "":
            return True
        if new_len > original_len:
            return False\
        
        j = 0

        for i in range(original_len):
            if t[i] == s[j]:
                if j == new_len -1:
                    return True
                j+=1
        return False

s1 = Solution()
s = "axc"
t= "ahbgdc"

print(s1.isSubsequence(s, t))

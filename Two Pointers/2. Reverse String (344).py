class Solution:
    def reverseString(self, s):
        length = len(s)-1

        l = 0
        r = length

        while l<=r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            r-=1
            l+=1
        return s



x = Solution()
s = ["h","e","l","l","o"]
print(x.reverseString(s))
s = ["H","a","n","n","a","h"]
print(x.reverseString(s))
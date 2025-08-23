class Solution:
    def isPalindrome(self, s):
        s = s.strip().replace(', ', '').split()
        print(s)


x=Solution()
s = "A man, a plan, a canal: Panama"
print(x.isPalindrome(s))

s = "race a car"
print(x.isPalindrome(s))

s = " "
print(x.isPalindrome(s))
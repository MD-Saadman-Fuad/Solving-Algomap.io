class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        dict1 = Counter(s)
        dict2 = Counter(t)
        if len(dict1)!=len(dict2):
            return False
        if dict1==dict2:
            return True
        return False
x = Solution()

s = "anagram"
t = "nagaram"
print(x.isAnagram(s, t))

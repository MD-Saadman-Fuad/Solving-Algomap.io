class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
# Brute Force
        # ransomeNote = sorted(ransomNote)
        # magazine = sorted(magazine)
        # count = 0
        # for i in range(len(magazine)):
        #     if magazine[i] == ransomeNote[count]:
        #         count+=1
        #         if count==len(ransomeNote):
        #             return True

        # return False

# O(R+M)
        from collections import Counter

        counter = Counter(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] in counter:
                if counter[ransomNote[i]] > 0:
                    counter[ransomNote[i]] -= 1
                else:
                    return False
            else:
                return False

        return True

#Top Code from leetcode

        # from collections import Counter
        # st1, st2 = Counter(ransomNote), Counter(magazine)
        # if st1 & st2 == st1:
        #     # print(st1 & st2)
        #     return True
        # return False

s = Solution()

print(s.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
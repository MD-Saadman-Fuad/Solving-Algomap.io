class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        flag = False
        needleCounter = 0
        needleLen = len(needle)
        startIndex = -1
        result = []
        for i in range(len(haystack)):
            if haystack[i] == needle[needleCounter]:
                flag = True
                needleCounter +=1
                if needleCounter == 1:
                    startIndex = i
                if needleCounter == needleLen:
                    result.append([startIndex, i])
                    needleCounter = 0
            else:
                flag = False
                needleCounter = 0
                startIndex = -1
        
        
            
        if result:
            return result[0][0] 
        else:
            return -1


haystack = "sadbutsad"
needle = "sad"
x  = Solution()
print(x.strStr(haystack, needle))




class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        matching = Counter('balloon')
        chars = Counter(text)
        min_count = []

        for key in matching:
            
            if key in chars:
                doable = chars[key]//matching[key]
                if doable == 0:
                    return 0
                else:
                    min_count.append(doable)
            else:
                return 0
        return min(min_count)


x=Solution()

text = 'ballon'
print(x.maxNumberOfBalloons(text))
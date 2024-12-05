class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#O(n*m)
        # count=0
        # for i in stones:
        #     if i in jewels:
        #         count+=1
        # return count
#O(n+m)
        jewel_set = set(jewels)
        count = 0
        for i in stones:
            if i in jewel_set:
                count+=1
        return count


s = Solution()
jewels = "z"
stones = "ZZ"
print(s.numJewelsInStones(jewels, stones))
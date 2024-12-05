class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        
#brute force approach    
        # max1 = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]

        #         if profit > 0:
        #             max1 = max(max1, profit)
        
        # return max1

# O(n) approach 
 
        max1 = 0
        min_price = prices[0]

        for i in prices:
            if i < min_price:
                min_price = i
            
            profit = i - min_price

            if profit >  max1:
                max1 = profit
            
        return max1

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))

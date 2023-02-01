from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = None
        max_profit = 0
        
        for i in range(len(prices)):
            price = prices[i]
            
            if not min_index or price < prices[min_index]:
                min_index = i
            else:
                profit = price - prices[min_index]
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit

sln = Solution().maxProfit([1, 2])
print(sln)
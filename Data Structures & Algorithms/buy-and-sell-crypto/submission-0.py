class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        n = len(prices)

        for i in range(n):
            res = max(res , prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        minPrice = prices[0]

        for i in range(1, n):
            res = max(res, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return res
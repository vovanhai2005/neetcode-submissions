class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        for i in range(1 , amount + 1):
            for j in range(n):
                if i >= coins[j]:
                    dp[i] = min(dp[i] , dp[i - coins[j]] + 1)
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
            


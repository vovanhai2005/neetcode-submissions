class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        dp = [1] * n
        for i in range(n):
            for j in range(i + 1 , n):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        for i in range(n):
            res = max(res , dp[i])
            print(dp[i])
        return res
class Solution:
    def rob_range(self, l: int, r: int, nums: List[int]) -> int:
        if l == r:
            return nums[l]
            
        n = len(nums)
        dp = [0] * n

        dp[l] = nums[l]
        dp[l + 1] = max(nums[l], nums[l + 1])

        for i in range(l + 2, r + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[r]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.rob_range(0 , n - 2, nums) , self.rob_range(1 , n - 1, nums))
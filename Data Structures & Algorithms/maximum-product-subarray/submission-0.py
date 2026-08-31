class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        valMin, valMax = 1, 1

        for i in range(n):
            tmp = valMax * nums[i]
            valMax = max(nums[i] * valMax, nums[i] * valMin, nums[i])
            valMin = min(tmp, nums[i] * valMin, nums[i])
            res = max(res , valMin, valMax)
        
        return res
            
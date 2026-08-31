class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        left[0] = nums[0]
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1 , len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in range(len(nums) - 2 , -1 , -1):
            right[i] = right[i + 1] * nums[i]
        
        res = [1] * len(nums)
        res[0] = right[1]
        res[len(nums) - 1] = left[len(nums) - 2]
        for i in range(1 , len(nums) - 1):
            res[i] = left[i - 1] * right[i + 1]
        return res

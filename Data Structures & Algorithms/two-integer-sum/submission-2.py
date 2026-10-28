class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        tmp = {}
        for i in range(n):
            tmp[nums[i]] = i
        
        for i in range(n):
            diff = target - nums[i]
            if diff in tmp and tmp[diff] != i:
                return list({i , tmp[diff]})
        
        return []
        
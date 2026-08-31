class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}

        for i, n in enumerate(nums):
            tmp[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in tmp and tmp[diff] != i:
                return [i , tmp[diff]]
        return []

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(id, currentArr, sum):
            if sum == target:
                res.append(currentArr.copy())
                return
            
            if id >= len(nums) or sum > target:
                return
            
            currentArr.append(nums[id])
            backtrack(id, currentArr, sum + nums[id])
            currentArr.pop()
            backtrack(id + 1, currentArr, sum)
        
        backtrack(0, [], 0)
        return res
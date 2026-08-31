class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(id, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            
            for i in range(id , len(nums)):
                if sum + nums[i] > target:
                    return
                curr.append(nums[i])
                backtrack(i, curr, sum + nums[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return res
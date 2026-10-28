class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0

        for x in nums:
            if x - 1 not in arr:
                cnt = 1
                while x + cnt in arr:
                    cnt += 1
                res = max(res , cnt)
                
        return res
            
        


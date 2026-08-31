class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        arr = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in arr:
                cnt = 1
                while (num + cnt) in arr:
                    cnt += 1
                res = max(res , cnt)
        return res

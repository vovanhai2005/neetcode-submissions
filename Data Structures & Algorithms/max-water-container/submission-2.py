class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        i, j = 0, n - 1
        
        while i < j:
            cnt = j - i
            if heights[i] >= heights[j]:
                res = max(res , heights[j] * cnt)
                j -= 1
            else:
                res = max(res , heights[i] * cnt)
                i += 1

            # print(i , j, res)
        return res
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prevHeight:
                return

            visit.add((r , c))
            dfs(r + 1 , c , visit, heights[r][c])
            dfs(r - 1 , c , visit, heights[r][c])
            dfs(r , c + 1 , visit, heights[r][c])
            dfs(r , c - 1 , visit, heights[r][c])

        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i , n - 1 , atlantic, heights[i][n - 1])
        
        for i in range(n):
            dfs(0, i , pacific, heights[0][i])
            dfs(m - 1, i , atlantic, heights[m - 1][i])
        
        for i in range(m):
            for j in range(n):
                if (i , j) in pacific and (i , j) in atlantic:
                    res.append((i , j))
        
        return res
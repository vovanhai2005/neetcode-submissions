class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        dir = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]

        def dfs(r , c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dR, dC in dir:
                dfs(r + dR, c + dC)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i , j)

        return res
                
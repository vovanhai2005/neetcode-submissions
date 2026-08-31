class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        dir = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]
        
        def bfs(r , c):
            q = deque()
            grid[r][c] = "0"
            q.append((r , c))

            while q:
                row, col = q.popleft()
                for dRow, dCol in dir:
                    nRow, nCol = row + dRow, col + dCol
                    if nRow < 0 or nCol < 0 or nRow >= m or nCol >= n or grid[nRow][nCol] == "0":
                        continue
                    q.append((nRow, nCol))
                    grid[nRow][nCol] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i , j)

        return res
                
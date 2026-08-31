class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = set()
        def backtrack(i, j, cnt):
            if cnt == len(word):
                return True

            if (min(i, j) < 0 or i >= m or 
            j >= n or word[cnt] != board[i][j] or (i , j) in visit):
                return False

            visit.add((i , j))
            res = (backtrack(i + 1 , j , cnt + 1) or
                   backtrack(i - 1 , j , cnt + 1) or
                   backtrack(i , j + 1 , cnt + 1) or
                   backtrack(i , j - 1 , cnt + 1))
            visit.remove((i , j))
            return res
             
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
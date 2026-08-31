class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                res += 1
                dfs(i)
        
        return res

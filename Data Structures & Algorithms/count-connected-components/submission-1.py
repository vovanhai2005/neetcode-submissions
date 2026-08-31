class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            queue = deque([node])
            visit[node] = True

            while queue:
                tmp = queue.popleft()
                
                for neighbor in adj[tmp]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        queue.append(neighbor)
            
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                res += 1
                bfs(i)
        
        return res

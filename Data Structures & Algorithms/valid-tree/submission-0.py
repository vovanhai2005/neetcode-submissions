class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        visited = set()

        adj = [[] for _ in range(n)]

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(root, parent):
            if root in visited:
                return False
            visited.add(root)

            for neighbor in adj[root]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, root):
                    return False
            
            return True
        
        return dfs(0 , -1) and len(visited) == n
                

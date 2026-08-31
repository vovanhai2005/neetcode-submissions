class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue = deque()
        visited = set()

        queue.append((0 , -1))
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                visited.add(neighbor)
                queue.append((neighbor , node))
            
        return len(visited) == n
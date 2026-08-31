class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        
        visited = set()

        def dfs(vertex):
            if vertex in visited:
                return False
            
            if adj[vertex] == []:
                return True
            visited.add(vertex)
            
            for adjVertex in adj[vertex]:
                if not dfs(adjVertex):
                    return False

            visited.remove(vertex)
            adj[vertex] = []
            return True
            
        for vertex in range(numCourses):
            if not dfs(vertex):
                return False
        return True
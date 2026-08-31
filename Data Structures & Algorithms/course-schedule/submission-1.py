class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        DAGcourse = 0
        while queue:
            node = queue.popleft()
            DAGcourse += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return DAGcourse == numCourses
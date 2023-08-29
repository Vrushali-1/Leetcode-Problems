class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        queue = collections.deque()
        graph = defaultdict(list)

        for course,pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)

        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbors in graph[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        return count == numCourses
        


        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        queue = collections.deque()
        graph = defaultdict(list)
        order = []

        for course,pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)

        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbors in graph[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        return order if len(order) == numCourses else []
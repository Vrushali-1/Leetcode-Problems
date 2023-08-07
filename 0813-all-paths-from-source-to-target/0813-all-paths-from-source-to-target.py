class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(current_node,path):
            if current_node == target:
                answer.append(path[:])
                return
            
            for next_node in graph[current_node]:
                path.append(next_node)
                backtrack(next_node,path)
                path.pop()
        
        path,answer = [0], []
        target = len(graph) - 1
        backtrack(0,path)
        return answer
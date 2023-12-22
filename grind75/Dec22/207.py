from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        # recursive
        edges = defaultdict(list)
        for course1, course2 in prerequisites:
            edges[course1].append(course2)
        
        visited = [-1] * numCourses

        def hasCycle(course):
            if visited[course] == 1:
                return False
            if visited[course] == 0:
                return True
            
            visited[course] = 0
            for edge in edges[course]:
                if hasCycle(edge):
                    return True
            visited[course] = 1
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True

class Solution:
    
    #makes adjacency List for the graph
    #time: O(V + E)
    #space: O(V + E)
    def adjacencyList(self, numCourses, prerequisites):
        
        l = [[] for i in range(numCourses)]
        
        for c1, c2 in prerequisites:
            l[c2].append(c1)
        
        return l
        
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #time: O(V + E)
        #space: O(V + E)
        
        #graph
        #return False if a graph has cycles
        
        #num Courses represent the number of nodes in the graph
        #we want to perform DFS for each node to see if there are cycles
        
        #DFS
        al = self.adjacencyList(numCourses, prerequisites)
        vertices = [0 for i in range(numCourses)]
        
        def hasCycle(v):
            
            #if we have already determined this node has no cycle
            if vertices[v] == 1:
                return False
            
            #this node has been visited before and we are visiting it again, cycle
            if vertices[v] == -1:
                return True
            
            vertices[v] = -1
            
            for course in al[v]:
                if hasCycle(course):
                    return True
                
            vertices[v] = 1
            return False
        

        for course in range(numCourses):
            if hasCycle(course):
                return False
            
        return True
                
            
            
            
            
        
        
        
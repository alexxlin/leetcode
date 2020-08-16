class Solution:
    
    #create an in-degree dictionary
    def in_degree(self, al):

        d = {}
        for node in al:
            for out_node in node:
                if out_node not in d:
                    d[out_node] = 1
                else:
                    d[out_node] += 1
                

        return d
            
    #create an out-degree adjacency list
    
    #time: O(E)
    #space: O(E) looking through all edges
    
    def adjacencyList(self, numCourses, prerequisites):

        l = [[] for i in range(numCourses)]

        for c1, c2 in prerequisites:

            l[c2].append(c1)
            
        return l
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #return topological ordering
        #use Kahn's algorithm
        
        #time: O(V + E)
        #space: O(V + E)
        
        #construct adjacency List and in degrees mapping
        al = self.adjacencyList(numCourses, prerequisites)
        in_degrees = self.in_degree(al)
        
        #space: O(E) worst case all nodes have zero degrees
        zero_degrees = []
        
        for node in range(len(al)):
            if not node in in_degrees:
                zero_degrees.append(node)
        
        result = []
        
        while zero_degrees:
            
            v = zero_degrees.pop()
            result.append(v)
            
            for out in al[v]:
                
                in_degrees[out] -= 1
                if in_degrees[out] == 0:
                    zero_degrees.append(out)
        
        if len(result) < numCourses:
            return [] 
        return result
                
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        #time: O(V ** 2 + E)
        #space: O(V + E)
        
        #at most 100 nodes, 6000 edges
        #shortest path, use Dijkstra
        
#         graph = {k[0]: [] for k in times}
        
#         for u, v, w in times:
            
#             graph[u].append([v, w])
        
        
        #Dijkstra
        
        # unvisited = [i for i in range(1, N + 1)]
        # distance = {i:math.inf for i in range(1, N + 1)}
        
#         distance[K] = 0
        
#         while True:
            
#             closest_node = -1
#             closest_distance = math.inf
            
#             for i in unvisited:
                
#                 if distance[i] < closest_distance:
                    
#                     closest_node = i
#                     closest_distance = distance[i]
            
#             #no nodes are found
#             if closest_node == -1:
#                 break
            
#             for v, w in graph.get(closest_node, []):
#                 distance[v] = min(distance[v], distance[closest_node] + w)
                
#             unvisited.remove(closest_node)
            
#         result = max(distance.values())
        
#         return result if result < math.inf else -1

        #Dijkstra with DFS heap (heap to store smallest distance)
    
        #time: O(VlogV + E)
        #space: O(V + E)
        
        graph = {k[0]: [] for k in times}
        
        for u, v, w in times:
            
            graph[u].append([v, w])
        
        import heapq
        
        heap = [(0, K)]
        distance = {i:math.inf for i in range(1, N + 1)}
        
        while heap:
            
            d, node = heapq.heappop(heap)
            
            if d < distance[node]:
                distance[node] = d
                
                for node, w in graph.get(node, []):
                    heapq.heappush(heap, [d + w, node])
                    
        result = max(distance.values())
        
        return result if result < math.inf else -1
            
            
            
            
                    
                    
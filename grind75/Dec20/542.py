from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs
        q = deque()
        m = len(mat)
        n = len(mat[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.appendleft((i, j, 0))
                else:
                    mat[i][j] = math.inf
        
        while q:
            i,j,d = q.pop()
            if mat[i][j] > d:
                mat[i][j] = d
            
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n 
and mat[new_i][new_j] > (d+1):
                    q.appendleft((new_i,new_j,d+1))
            
        return mat

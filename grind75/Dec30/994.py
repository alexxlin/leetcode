from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q = deque()
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.appendleft((i, j))
        
        while q:
            time += 1
            for _ in range(len(q)):
                i, j = q.pop()
                for dx, dy in directions:
                    new_i = i + dx
                    new_j = j + dy
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j 
< n and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        q.appendleft((new_i, new_j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
    
        return max(time, 0)

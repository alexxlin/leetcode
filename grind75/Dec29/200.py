class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # dfs
        # O(mn), O(mn)
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(grid, i, j):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        
        return count

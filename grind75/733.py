class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: 
int) -> List[List[int]]:
        # dfs
        stack = []
        stack.append([sr, sc])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        visited = set()
        while stack:
            r, c = stack.pop()
            if r < 0 or r >= m or c < 0 or c >= n:
                continue
            
            if image[r][c] != old_color:
                continue
            
            image[r][c] = color
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (new_r, new_c) not in visited:
                    stack.append([new_r, new_c])
                    visited.add((new_r, new_c))
        
        return image

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        direction_order = {(0,1):(1,0), (1,0):(0,-1), 
(0,-1):(-1,0),(-1,0):(0,1)}
        i, j = 0, 0
        m = len(matrix)
        n = len(matrix[0])
        direction = (0,1)
        while True:
            print(f"{i} {j}")
            result.append(matrix[i][j])
            # equivalent to setting it to seen
            matrix[i][j] = 101
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and 
matrix[new_i][new_j] != 101:
                i = new_i
                j = new_j
            # change direction
            else:
                direction = direction_order[direction]
                new_i = i + direction[0]
                new_j = j + direction[1]
                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n 
and matrix[new_i][new_j] != 101:
                    i = new_i
                    j = new_j
                # if changing direction still gives invalid result, we 
have reached the end
                else:
                    return result


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j, index):
            if index == l:
                return True

            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == 
word[index]:
                board[i][j] = '#'
                for x, y in directions:
                    new_i = i+x
                    new_j = j+y
                    if dfs(new_i, new_j, index+1):
                        return True
                board[i][j] = word[index]
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


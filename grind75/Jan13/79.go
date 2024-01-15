func exist(board [][]byte, word string) bool {
    dirs := [][]int{
        []int{1,0}, []int{0,1}, []int{-1,0}, []int{0,-1},
    }
    m, n := len(board), len(board[0])
    visited := make([]int, m*n)
    var dfs func(int, int, int) bool 

    dfs = func(idx int, i int, j int) bool {
        // fmt.Printf("idx = %d, letter = %v\n", idx, string(board[i][j]))
        // fmt.Println(visited)
        if word[idx] != board[i][j] {
            return false
        }
        if idx == len(word)-1 {
            return true
        }

        for _, dir := range dirs {
            ni, nj := i+dir[0], j+dir[1]
            if ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni*n+nj] == 1 {
                continue
            }
            visited[ni*n+nj] = 1
            if dfs(idx+1, ni, nj) {
                return true
            }
            visited[ni*n+nj] = 0
        }
        return false
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if board[i][j] != word[0] { continue }
            if len(word) == 1 { return true }
            visited[i*n+j] = 1
            if dfs(0,i,j) {
                return true
            }
            visited[i*n+j] = 0
        }
    }
    return false
}

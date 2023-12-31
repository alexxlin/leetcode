func numIslands(grid [][]byte) int {
    m,n := len(grid), len(grid[0])
    dirs := [][]int{[]int{1,0}, []int{-1,0}, []int{0,1}, []int{0,-1},}
    visited := make([]int, m*n)
    ret := 0   
    var dfs func(int, int)
    
    dfs = func(i,j int) {
        for _, dir := range dirs {
            ni, nj := i+dir[0], j+dir[1]
            if ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni*n+nj] == 1 || grid[ni][nj] == '0' {
                continue
            }
            visited[ni*n+nj] = 1
            dfs(ni, nj)
        }
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if visited[i*n+j] == 1 || grid[i][j] == '0' {
                continue
            }
            ret += 1
            dfs(i,j)
        }
    }

    return ret
}

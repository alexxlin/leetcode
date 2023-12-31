func orangesRotting(grid [][]int) int {
    dirs := [][]int{[]int{1,0}, []int{-1,0}, []int{0,1}, []int{0,-1},}
    q := [][]int{}
    m,n := len(grid), len(grid[0])
    cnt := 0
    visited := make([]int, m*n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 2 { 
                q = append(q, []int{i,j})
                visited[i*n+j] = 1
            }
            if grid[i][j] == 1 {
                cnt += 1
            }
        }
    }
    if cnt == 0 { return cnt }
    ret := 0
    for len(q) > 0 {
        ret += 1
        cq := [][]int{}
        lq := len(q)
        for lq > 0 {
            i,j := q[0][0], q[0][1]
            q = q[1:]
            lq--
            for _, dir := range dirs {
                ni, nj := i+dir[0], j+dir[1]
                if ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni*n+nj] == 1 {
                    continue
                }
                if grid[ni][nj] != 1 {
                    continue
                }
                cq = append(cq, []int{ni, nj})
                visited[ni*n+nj] = 1
                cnt -= 1
                if cnt == 0 {
                    return ret
                }
            }
        }
        q = cq
        
    }
    return -1
}

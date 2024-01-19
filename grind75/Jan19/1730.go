func getFood(grid [][]byte) int {
    m,n := len(grid), len(grid[0])
    visited := make([]int, m*n)
    dirs := [][]int{[]int{1,0}, []int{0,1}, []int{-1,0}, []int{0,-1}}
    q := [][]int{}
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] != '*' {
                continue
            }
            q = append(q, []int{i,j})
            visited[i*n+j] = 1
            break
        }
    }
    ret := 0
    for len(q) > 0 {
        lq := len(q)
        cq := [][]int{}
        for lq > 0 {
            i,j := q[0][0], q[0][1]
            q = q[1:]
            lq--
            for _, dir := range dirs {
                ni,nj := i+dir[0],j+dir[1]
                if ni < 0 || ni >=m || nj < 0 || nj >= n {
                    continue
                }
                if visited[ni*n+nj] == 1 { continue }
                m := grid[ni][nj]
                if m == '#' {
                    return ret+1
                }
                if m == 'X' {
                    continue
                }
                visited[ni*n+nj] = 1
                cq = append(cq, []int{ni,nj})
            }
        }
        q = cq
        ret++
    }
    return -1
}

func updateMatrix(mat [][]int) [][]int {
    dirs := [][]int{[]int{0,1}, []int{0,-1}, []int{1,0}, []int{-1,0},}
    m,n := len(mat), len(mat[0])
    visited := make([]int, m*n)
    q := [][]int{}
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 0 {
                q = append(q, []int{i,j})
                visited[i*n+j] = 1
            }
        }
    }
    dist := 0
    for len(q) > 0 {
        cq := [][]int{}
        lq := len(q)
        dist += 1
        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--
            i,j := node[0], node[1]
            for _, dir := range dirs {
                ni,nj := i+dir[0], j+dir[1]
                if ni < 0 || ni >= m || nj < 0 || nj >= n { continue }
                if visited[ni*n+nj] == 1 { continue }
                visited[ni*n+nj] = 1
                mat[ni][nj] = dist
                cq = append(cq, []int{ni,nj})
            }
        }
        q = cq
    }
    return mat
}

func pacificAtlantic(heights [][]int) [][]int {
    m,n := len(heights), len(heights[0])
    ret := [][]int{}
    v := make([]int, m*n)
    vmap := map[int]struct{}{}
    dirs := [][]int{[]int{1,0}, []int{0,1}, []int{-1,0}, []int{0,-1},}
    var dfs func(int, int, bool) 
    dfs = func(i,j int, judge bool) {
        if judge {
            if _, ok := vmap[i*n+j]; ok {
                ret = append(ret, []int{i,j})
            }
        }
        for _, dir := range dirs {
            ni,nj := i+dir[0], j +dir[1]
            if ni < 0 || ni >= m || nj < 0 || nj >= n || v[ni*n+nj] == 1 { continue }
            if heights[i][j] > heights[ni][nj] { continue }
            if !judge {
                vmap[ni*n+nj] = struct{}{}
            }
            v[ni*n+nj] = 1
            dfs(ni,nj, judge)
        }
    }

    // pacific
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i != 0 && j != 0 { continue }
            if v[i*n+j] == 1 { continue }
            vmap[i*n+j] = struct{}{}
            v[i*n+j] = 1
            dfs(i,j, false)
        }
    }
    // fmt.Println(vmap)
    v = make([]int, m*n)
    // atlantic
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i != m-1 && j != n-1 { continue }
            if v[i*n+j] == 1 { continue }
            // vmap[i*n+j] = struct{}{}
            v[i*n+j] = 1
            dfs(i,j, true)
        }
    }

    return ret
}

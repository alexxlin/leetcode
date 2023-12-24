func swimInWater(grid [][]int) int {
    dirs := [][]int{[]int{0,1}, []int{0,-1}, []int{1,0}, []int{-1,0},}
    n := len(grid)
    l,r := 0, n*n-1
    ret := n*n-1
    for l <= r {
        mid := l+(r-l)>>1
        if grid[0][0] > mid {
            l = mid+1
            continue
        }
        visited := make([]int, n*n)
        visited[0] = 1
        q := [][]int{[]int{0,0}}
        for len(q) > 0 {
            lq := len(q)
            cq := [][]int{}
            for lq > 0 {
                i,j := q[0][0], q[0][1]
                q = q[1:]
                lq--
                for _, dir := range dirs {
                    ni, nj := i+dir[0], j+dir[1]
                    if ni < 0 || ni >= n || nj < 0 || nj >= n || visited[ni*n+nj] == 1 {
                        continue
                    }
                    if grid[ni][nj] > mid {
                        continue
                    }
                    visited[ni*n+nj] = 1
                    cq = append(cq, []int{ni,nj})
                }
            }
            q = cq
        }
        if visited[n*n-1] == 1 {
            r = mid-1
            ret = min(ret, mid)
        } else {
            l = mid+1
        }
    }
    return ret
}

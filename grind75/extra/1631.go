func abs(x, y int) int {
    if x >= y {
        return x-y
    }
    return y-x
}
func minimumEffortPath(heights [][]int) int {
    dirs := [][]int{[]int{0,1}, []int{1,0}, []int{0,-1}, []int{-1,0},}
    l,r := 0, 999999
    ret := 0
    m,n := len(heights), len(heights[0])
    for l <= r {
        mid := l+(r-l)>>1
        visited := make([]int, m*n)
        q := [][]int{[]int{0,0}}
        visited[0] = 1
        for len(q) > 0 {
            lq := len(q)
            cq := [][]int{}
            for lq > 0 {
                node := q[0]
                q = q[1:]
                lq--
                i,j := node[0], node[1]
                for _, dir := range dirs {
                    ni, nj := i+dir[0], j+dir[1]
                    if ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni*n+nj] == 1 {
                        continue
                    }
                    if abs(heights[i][j], heights[ni][nj]) > mid { 
                        continue
                    }
                    visited[ni*n+nj] = 1
                    cq = append(cq, []int{ni,nj})
                }
            }
            q = cq
        }
        if visited[m*n-1] == 1{
            ret = mid
            r = mid-1
        } else {
            l = mid+1
        }
    }
    return ret
}

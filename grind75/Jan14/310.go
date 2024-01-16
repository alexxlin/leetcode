func findMinHeightTrees(n int, edges [][]int) []int {
    if n == 0 { return []int{} }
    if n == 1 { return []int{0} }
    g := map[int][]int{}
    in := make([]int, n)

    for _, edge := range edges {
        g[edge[0]] = append(g[edge[0]], edge[1])
        g[edge[1]] = append(g[edge[1]], edge[0])
        in[edge[0]]++
        in[edge[1]]++
    }
    q := []int{}
    for key, val := range in {
        if val == 1 {
            q = append(q, key)
        }
    }
    ret := q
    for len(q) > 0 {
        cq := []int{}
        lq := len(q)

        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--
            for _, cn := range g[node] {
                in[cn]--
                if in[cn] == 1 {
                    cq = append(cq, cn)
                }
            }
        }
        if len(cq) != 0 {
            ret = cq
        }
        q = cq
    }
    return ret
}

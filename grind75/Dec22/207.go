
func canFinish(numCourses int, prerequisites [][]int) bool {
    g := make([][]int, numCourses)
    in := make([]int, numCourses)
    for _, c := range prerequisites {
        g[c[1]] = append(g[c[1]], c[0])
        in[c[0]] += 1
    }
    q := []int{}
    ret := []int{}
    for i := 0; i < numCourses; i++ {
        if in[i] == 0 {
            q = append(q, i)
            ret = append(ret, i)
        }
    }

    for len(q) > 0 {
        cq := []int{}
        lq := len(q)

        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--

            for _, next := range g[node] {
                in[next] -= 1
                if in[next] == 0 {
                    ret = append(ret, next)
                    cq = append(cq, next)
                }
            }
        }
        q = cq
    }
    return len(ret) == numCourses
}

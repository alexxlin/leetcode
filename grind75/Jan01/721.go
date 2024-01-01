func accountsMerge(accounts [][]string) [][]string {
    g := map[string][]string{}
    ret := [][]string{}
    visited := map[string]struct{}{}
    // construct g
    for _, account := range accounts {
        name := account[0]
        for i := 1; i < len(account); i++ {
            a := name+"#"+account[i]
            if len(account) == 2 {
                g[a] = []string{}
                continue
            }
            for j := i+1; j < len(account); j++ {
                b := name+"#"+account[j]
                g[a] = append(g[a], b)
                g[b] = append(g[b], a)
            }
        }
    }
    
    for key, _ := range g {
        if _, ok := visited[key]; ok {
            continue
        }
        ss := strings.Split(key, "#")
        name, tmp := ss[0], []string{ss[1]}
        q := []string{key}
        visited[key] = struct{}{}
        for len(q) > 0 {
            cq := []string{}
            lq := len(q)
            for lq > 0 {
                node := q[0]
                q = q[1:]
                lq--
                for _, next := range g[node] {
                    if _, ok := visited[next]; ok {
                        continue
                    }
                    cq = append(cq, next)
                    tmp = append(tmp, strings.Split(next, "#")[1])
                    visited[next] = struct{}{}
                }
            }
            q = cq
        }
        sort.Strings(tmp)
        ret = append(ret, append([]string{name}, tmp...))
    }
    return ret
}

func canCross(stones []int) bool {
    if stones[1] != 1 { return false }
    m := map[int]bool{}
    var dfs func(int, int) bool
    dfs = func(idx, step int) bool {
        if idx == len(stones)-1 {
            return true
        }
        key := idx*1000+step
        for i := idx+1; i < len(stones); i++ {
            
            if _, ok := m[key]; ok {
                return m[key]
            }
            dist := stones[i]-stones[idx]
            if dist >= step-1 && dist <= step+1 {
                if dfs(i, dist) {
                    m[key] = true
                    return true
                }
            } else if dist > step+1 {
                m[key] = false
                return false
            }
        }
        return false
    }
    return dfs(0,0)
}

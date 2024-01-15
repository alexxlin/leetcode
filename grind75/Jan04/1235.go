func jobScheduling(startTime []int, endTime []int, profit []int) int {
    jobs := [][]int{}
    n := len(startTime)
    for i := 0; i < n; i++ {
        jobs = append(jobs, []int{startTime[i], endTime[i], profit[i]})
    }
    sort.Slice(jobs, func(i, j int) bool {
        return jobs[i][0] < jobs[j][0]
    })
    mem := map[int]int{}

    var dfs func(int) int
    dfs = func(idx int) int {
        if idx < 0 { return 0 }
        end, profit := jobs[idx][1], jobs[idx][2]
        if idx == n-1 {
            return profit
        }
        if val, ok := mem[idx]; ok {
            return val
        }
        
        curmax := dfs(idx+1)

        l,r := idx+1, n-1
        for l < r {
            m := l+(r-l)>>1
            if jobs[m][0] >= end {
                r = m
           } else {
               l = m+1
           }
        }
        if jobs[r][0] < end { r = -1 }
        ret := max(curmax, profit+dfs(r))
        mem[idx] = ret
        return ret
    }

    return dfs(0)
}

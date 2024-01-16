func leastInterval(tasks []byte, n int) int {
    m := [26]int{}
    maxt := -1
    cnt := -1
    for _, c := range tasks {
        idx := int(c-'A')
        m[idx]++
        if m[idx] > maxt {
            maxt = m[idx]
            cnt = 1
        } else if m[idx] == maxt {
            cnt++
        }
        
    }
    
    return max(len(tasks), (maxt-1)*(n+1)+cnt)
}

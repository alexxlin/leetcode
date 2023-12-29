func coinChange(coins []int, amount int) int {
    q := []int{0}
    visited := map[int]struct{}{}
    visited[0] = struct{}{}
    sort.Ints(coins)
    cnt := 0
    for len(q) > 0 {
        cq := []int{}
        lq := len(q)
        for lq > 0 {
            cur := q[0]
            q = q[1:]
            lq--
            if cur == amount {
                return cnt
            }
            for _, val := range coins {
                if val+cur > amount {
                    break
                }
                if _, ok := visited[val+cur]; !ok {
                    visited[val+cur] = struct{}{}
                    cq = append(cq, val+cur)
                }
            }
        }
        q = cq
        cnt += 1
    }
    return -1
}

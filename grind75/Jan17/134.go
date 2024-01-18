// cheated, not solve by myself
func canCompleteCircuit(gas []int, cost []int) int {
    n := len(gas)
    for i := 0; i < n; {
        curgas, curcost, cnt := 0, 0, 0
        for cnt < n {
            idx := (i+cnt)%n
            curgas += gas[idx]
            curcost += cost[idx]
            if curgas <curcost {
                break
            }
            cnt++
        }
        if cnt == n {
            return i
        } else {
            i = i+cnt+1
        }
    }
    return -1
}

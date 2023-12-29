func longestPalindrome(s string) int {
    m := map[int]int{}
    ret := 0
    for _, c := range s {
        m[int(c-'a')] += 1
    }
    ifodd := false
    for _, val := range m {
        if val % 2 == 0 {
            ret += val
        } else {
            ifodd = true
            ret += (val-1)
        }
    }
    if ifodd { return ret + 1 }
    return ret
}

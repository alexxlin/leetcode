func lengthOfLongestSubstring(s string) int {
    l := len(s)
    if l == 0 { return l }
    m := map[byte]int{}
    i,j := 0,0
    ret := math.MinInt
    for j < l {
        if m[s[j]] == 0 {
            m[s[j]] += 1
            j++
            continue
        }
        ret = max(ret, j-i)
        for i < j {
            m[s[i]] -= 1
            i++
            if s[i-1] == s[j] {
                break
            }
        }
    }
    ret = max(ret, j-i)
    return ret
}

func minWindow(s string, t string) string {
    if len(s) < len(t) { return "" }
    ct := len(t)
    mt := map[int]int{}
    for _, c := range t {
        mt[int(c-'0')] += 1
    }
    rs := math.MaxInt
    ret := ""
    i, j := 0, 0
    for j < len(s) {
        if val, ok := mt[int(s[j]- '0')]; ok && val > 0 {
            ct -= 1
        }
        mt[int(s[j]- '0')] -= 1
        if ct == 0 {
            for mt[int(s[i]-'0')] < 0 {
                mt[int(s[i]-'0')] += 1
                i++
            }
            tmp := j-i+1
            if tmp < rs {
                rs = tmp
                ret = s[i:j+1]
            }
            mt[int(s[i]-'0')] += 1
            i++
            ct += 1
        }
        j++
    }
    return ret
}



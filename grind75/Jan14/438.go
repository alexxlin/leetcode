func findAnagrams(s string, p string) []int {
    ss, pp := [26]int{}, [26]int{}
    ret := []int{}
    if len(s) < len(p) {
        return ret
    }
    for _, c := range p {
        pp[int(c-'a')]++
    }
    l,r := 0, 0
    for r < len(p) {
        ss[int(s[r]-'a')]++
        r++
    }
    if ss == pp {
        ret = append(ret, l)
    }
    for r < len(s) {
        ss[int(s[l]-'a')]--
        ss[int(s[r]-'a')]++
        l++
        r++
        if ss == pp {
            ret = append(ret, l)
        }
    }
    return ret
}

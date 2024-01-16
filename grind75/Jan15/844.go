func backspaceCompare(s string, t string) bool {
    ss := []int{}
    st := []int{}

    for _, v := range s {
        if v == '#' && len(ss) > 0 {
            ss = ss[:len(ss)-1]
        } else if v != '#'{
            ss = append(ss, int(v-'a'))
        }
    }
    for _, v := range t {
        if v == '#' && len(st) > 0 {
            st = st[:len(st)-1]
        } else if v != '#' {
            st = append(st, int(v-'a'))
        }
    }
    if len(ss) != len(st) { return false }
    for i := 0; i < len(ss); i++ {
        if ss[i] != st[i] {
            return false
        }
    }
    return true
}

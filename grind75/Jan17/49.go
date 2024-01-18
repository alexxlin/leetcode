func groupAnagrams(strs []string) [][]string {
    m := map[[26]int][]string{}

    for _, str := range strs {
        cmap := [26]int{}
        for _, c := range str {
            cmap[c-'a']++
        }
        if _, ok := m[cmap]; ok {
            m[cmap] = append(m[cmap], str)
        } else {
            m[cmap] = []string{str}
        }
    }
    ret := [][]string{}
    for _, val := range m {
        ret = append(ret, val)
    }
    return ret
}

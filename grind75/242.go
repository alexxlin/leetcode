func isAnagram(s string, t string) bool {
    sm, tm := [27]int{}, [27]int{}
    if len(s) != len(t) {
        return false
    }
    for i := 0; i < len(s); i++ {
        sm[int(s[i]-'a')] += 1
        tm[int(t[i]-'a')] += 1
    }
    for i := 0; i < 27; i++ {
        if sm[i] != tm[i] {
            return false
        }
    }
    return true
}

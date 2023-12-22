func canConstruct(ransomNote string, magazine string) bool {
    m := [26]int{}
    for _, c := range magazine {
        m[int(c-'a')] += 1
    }
    for _, c := range ransomNote {
        idx := int(c-'a')
        if m[idx] <= 0 { return false}
        m[idx] -= 1
    }
    return true
}

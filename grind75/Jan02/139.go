func wordBreak(s string, wordDict []string) bool {
    m := map[string]bool{}
    var dfs func(string) bool
    dfs = func (cur string) bool {
        k := cur
        if cur == s {
            return true
        }
        if r, ok := m[k]; ok {
            return r
        }
        for i := 0; i < len(wordDict); i++ {
            if !strings.HasPrefix(s, cur+wordDict[i]) {
                continue
            }
            if dfs(cur+wordDict[i]) {
                m[k] = true
                return true
            }
        }
        m[k] = false
        return false
    }
    return dfs("")
}

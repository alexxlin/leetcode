func letterCombinations(digits string) []string {
    if digits == "" { return []string{} }
    m := map[int]string{
        2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs",
        8:"tuv", 9:"wxyz",
    }
    ret := []string{}
    var dfs func(string, int)
    dfs = func(cur string, idx int) {
        if idx == len(digits) {
            ret = append(ret, cur)
            return
        }
        d := int(digits[idx] - '0')
        for _, c := range m[d] {
            dfs(cur+string(c), idx+1)
        }
    }
    dfs("", 0)
    return ret
}

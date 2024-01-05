func longestPalindrome(s string) string {
    l := len(s)
    if l == 1 {
        return s
    }
    ret := ""
    maxsize := math.MinInt
    for i := 0; i < l-1; i++ {
        lptr, rptr := i-1, i+1
        for rptr < l && s[rptr] == s[rptr-1]{
            rptr++
        }

        for lptr >= 0 && rptr < l && s[lptr] == s[rptr] {
            lptr--
            rptr++
        }
        cursize := rptr-lptr-1
        if cursize > maxsize {
            maxsize = cursize
            ret = s[lptr+1:lptr+1+maxsize]
        }
    }
    return ret
}

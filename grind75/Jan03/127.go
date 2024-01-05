func ladderLength(beginWord string, endWord string, wordList []string) int {
    visited := map[string]struct{}{}
    m := map[string][]string{}
    foundEnd := false
    for _, word := range wordList {
        if word == endWord {
            foundEnd = true
        }
        if word == beginWord {
            continue
        }
        for i := 0; i < len(word); i++ {
            k := word[:i]+"-"+word[i+1:]
            if _, ok := m[k]; ok {
                m[k] = append(m[k], word)
            } else {
                m[k] = []string{word}
            }
        }
    }
    if !foundEnd {
        return 0
    }
    q := []string{beginWord}
    ret := 0
    for len(q) > 0 {
        cq := []string{}
        lq := len(q)
        ret++
        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--
            if node == endWord {
                return ret
            }
            for i := 0; i < len(node); i++ {
                k := node[:i]+"-"+node[i+1:]
                if _, ok := m[k]; !ok {
                    continue
                }
                for _, word := range m[k] {
                    if _, ok := visited[word]; ok {
                        continue
                    }
                    cq = append(cq, word)
                    visited[word] =struct{}{}
                }
            }
        }
        q = cq
    }
    return 0
}

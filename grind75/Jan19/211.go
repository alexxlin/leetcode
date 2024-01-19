type node struct {
    val [26]*node
    end bool
}
type WordDictionary struct {
    head *node
}

func Constructor() WordDictionary {
    w := WordDictionary{}
    w.head = &node{}
    return w
}


func (w *WordDictionary) AddWord(word string)  {
    cur := w.head
    for _, c := range word {
        v := c-'a'
        if (cur.val)[v] == nil {
            (cur.val)[v] = &node{}
        }
        cur = (cur.val)[v]
    }
    cur.end = true
}


func (w *WordDictionary) Search(word string) bool {
    
    var dfs func(int, *node) bool 
    dfs = func(idx int, n *node) bool {
        if idx == len(word) {
            return n.end
        }
        if word[idx] != '.' {
            // fmt.Printf("idx:%d word:%s\n", idx, word)
            next := (n.val)[word[idx]-'a']
            if next != nil && dfs(idx+1, next) {
                return true
            }
        } else {
            for i := 0; i < len(n.val); i++ {
                next := (n.val)[i]
                if next != nil && dfs(idx+1, next) {
                    return true
                }
            }
        }
        return false
    }
    return dfs(0, w.head)
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

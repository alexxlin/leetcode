type Trie struct {
    end bool
    ptr [26]*Trie
}


func Constructor() Trie {
    return Trie{}
}


func (this *Trie) Insert(word string)  {
    cur := this
    for _, c := range word {
        if cur.ptr[int(c-'a')] == nil {
            cur.ptr[int(c-'a')] = &Trie{}
        }
        cur = cur.ptr[int(c-'a')]
    }
    cur.end = true
}


func (this *Trie) Search(word string) bool {
    cur := this
    for _, c := range word {
        if cur.ptr[int(c-'a')] == nil {
            return false
        }
        cur = cur.ptr[int(c-'a')]
    }
    return cur.end
}


func (this *Trie) StartsWith(prefix string) bool {
    cur := this
    for _, c := range prefix {
        if cur.ptr[int(c-'a')] == nil {
            return false
        }
        cur = cur.ptr[int(c-'a')]
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */

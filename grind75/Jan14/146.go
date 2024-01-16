 type node struct {
     k int
     v int
     prev *node
     next *node
 }

type LRUCache struct {
    head *node
    tail *node
    m map[int]*node
    cap int
    size int
}

func (this *LRUCache) insertToHead(n *node) {
    n.next = this.head.next
    n.prev = this.head
    n.next.prev = n
    this.head.next = n
}

func (this *LRUCache) remove(n *node) {
    n.prev.next = n.next
    n.next.prev = n.prev
}

func (this *LRUCache) moveToHead(n *node) {
    this.remove(n)
    this.insertToHead(n)
}

func (this *LRUCache) removeFromTail() {
    // size check has been conducted before calling this func
    n := this.tail.prev
    n.prev.next = n.next
    n.next.prev = n.prev
    delete(this.m, n.k)
}

func Constructor(capacity int) LRUCache {
    l := LRUCache{}
    l.head = &node{}
    l.tail = &node{}
    l.cap = capacity
    l.head.next = l.tail
    l.tail.prev = l.head
    l.m = make(map[int]*node)
    return l
}


func (this *LRUCache) Get(key int) int {
    
    if n, ok := this.m[key]; ok {
        this.moveToHead(n)
        // this.pr(this.head)
        return n.v
    } else {
        // this.pr(this.head)
        return -1
    }
}


func (this *LRUCache) Put(key int, value int)  {
    if n, ok := this.m[key]; ok {
        n.v = value
        this.moveToHead(n)
    } else {
        nn := &node{k:key, v:value}
        if this.size == this.cap {
            this.removeFromTail()
        } else {
            this.size++
        }
        this.insertToHead(nn)
        this.m[key] = nn
    }
    // this.pr(this.head)
}

func (this *LRUCache)pr(n *node) {
    ret := []string{}
    for n != nil {
        ret = append(ret, fmt.Sprintf("%d-%d", n.k, n.v))
        n = n.next
    }
    fmt.Println(strings.Join(ret, "->"))
    fmt.Println(this.m)
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

type hp struct {
    sort.IntSlice
}

func (h *hp) Push(v interface{}) {
    h.IntSlice = append(h.IntSlice, v.(int))
}

func (h *hp) Pop() interface{} {
    a := h.IntSlice
    v := a[len(a)-1]
    h.IntSlice = a[:len(a)-1]
    return v
}

type MedianFinder struct {
    highQ hp // higher portion
    lowQ hp // lower portion
    // lowQ >= highQ
}


func Constructor() MedianFinder {
    return MedianFinder{}
}


func (m *MedianFinder) AddNum(num int)  {
    lq, hq := &m.lowQ, &m.highQ
    if lq.Len() == 0 || num <= -1*lq.IntSlice[0] {
        // fmt.Printf("lowQ num = %d\n", num)
        heap.Push(lq, -1*num)
        
        if hq.Len()+1 < lq.Len() {
            heap.Push(hq, -1*heap.Pop(lq).(int))
        }
    } else {
        // fmt.Printf("highQ num = %d\n", num)
        heap.Push(hq, num)
        if hq.Len() > lq.Len() {
            tmp := -1*heap.Pop(hq).(int)
            heap.Push(lq, tmp)
        }
    }
    // fmt.Println(m.lowQ)
    // fmt.Println(m.highQ)
}


func (m *MedianFinder) FindMedian() float64 {
    if m.lowQ.Len() > m.highQ.Len() {
        return float64(-1*m.lowQ.IntSlice[0])
    }
    return float64(m.highQ.IntSlice[0]-m.lowQ.IntSlice[0]) / 2
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */

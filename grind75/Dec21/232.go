type MyQueue struct {
    s []int
    bs []int
}


func Constructor() MyQueue {
    return MyQueue{}
}


func (this *MyQueue) Push(x int)  {
    this.s = append(this.s, x)
}


func (this *MyQueue) Pop() int {
    if len(this.bs) == 0 {
        for len(this.s) > 0 {
            this.bs = append(this.bs, this.s[len(this.s)-1])
            this.s = this.s[:len(this.s)-1]
        }
    }
    ret := this.bs[len(this.bs)-1]
    this.bs = this.bs[:len(this.bs)-1]
    return ret
}


func (this *MyQueue) Peek() int {
    if len(this.bs) == 0 {
        for len(this.s) > 0 {
            this.bs = append(this.bs, this.s[len(this.s)-1])
            this.s = this.s[:len(this.s)-1]
        }
    }
    ret := this.bs[len(this.bs)-1]
    return ret
}


func (this *MyQueue) Empty() bool {
    return len(this.bs) == 0 && len(this.s) == 0
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */

type pair struct {
    t int
    v string
}

type TimeMap struct {
    m map[string][]pair
}


func Constructor() TimeMap {
    return TimeMap{map[string][]pair{}}
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    p := pair{t: timestamp, v: value}
    this.m[key] = append(this.m[key], p)
}


func (this *TimeMap) Get(key string, timestamp int) string {
    p, ok := this.m[key]
    if !ok {
        return ""
    }
    for i := len(p)-1; i >= 0; i-- {
        if p[i].t <= timestamp {
            s := p[i].v
            return s
        }
    }
    return ""
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */

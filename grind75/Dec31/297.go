/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
    
}

func Constructor() Codec {
    return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    if root == nil { return "" }
    ret := []string{}
    q := []*TreeNode{root}

    for len(q) > 0 {
        lq := len(q)
        cq := []*TreeNode{}

        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--

            lv, rv := -9999, -9999
            if node.Left != nil { 
                lv = node.Left.Val
                cq = append(cq, node.Left)
            }
            if node.Right != nil { 
                rv = node.Right.Val
                cq = append(cq, node.Right)
            }
            ret = append(ret, fmt.Sprintf("%d/%d/%d", node.Val, lv, rv))
        }
        q = cq
    }
    // fmt.Println(strings.Join(ret, "@"))
    return strings.Join(ret, "@")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {    
    if data == "" { return nil }
    decode := strings.Split(data, "@")
    root := &TreeNode{}
    q := []*TreeNode{root}

    for len(q) > 0 {
        cq := []*TreeNode{}
        lq := len(q)
        
        for lq > 0 {
            node := q[0]
            q = q[1:]
            info := decode[0]
            decode = decode[1:]
            lq--
            
            vals := strings.Split(info, "/")
            node.Val, _ = strconv.Atoi(vals[0])
            if vals[1] != "-9999" {
                val, _ := strconv.Atoi(vals[1])
                lnode := &TreeNode{Val: val}
                node.Left = lnode
                cq = append(cq, lnode)
            }
            if vals[2] != "-9999" {
                val, _ := strconv.Atoi(vals[2])
                rnode := &TreeNode{Val: val}
                node.Right = rnode
                cq = append(cq, rnode)
            }
        }
        q = cq
    }
    return root

}


/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */

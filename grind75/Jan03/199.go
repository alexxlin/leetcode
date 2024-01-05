/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    ret := []int{}
    if root == nil {
        return ret
    }
    q := []*TreeNode{root}
    level := 0
    for len(q) > 0 {
        cq := []*TreeNode{}
        lq := len(q)
        for lq > 0 {
            node := q[0]
            q = q[1:]
            lq--
            if len(ret) == level {
                ret = append(ret, node.Val)
            }
            if node.Right != nil {
                cq = append(cq, node.Right)
            }
            if node.Left != nil {
                cq = append(cq, node.Left)
            }
        }
        q = cq
        level += 1
    }
    return ret
}

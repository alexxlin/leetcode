/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    ret := [][]int{}
    if root == nil { return ret }

    q := []*TreeNode{root}
    for len(q) > 0 {
        nq := []*TreeNode{}
        lq := len(q)
        lret := []int{}
        for lq > 0 {
            node := q[0]
            q = q[1:]
            lret = append(lret, node.Val)
            if node.Left != nil {
                nq = append(nq, node.Left)
            }
            if node.Right != nil {
                nq = append(nq, node.Right)
            }
            lq--
        }
        ret = append(ret, lret)
        q = nq
    }
    return ret 
}

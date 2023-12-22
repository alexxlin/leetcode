/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    var dfs func(*TreeNode) int
    dfs = func(root *TreeNode) int {
        if root == nil { return 0 }
        l, r := dfs(root.Left), dfs(root.Right)
        if l == -1 || r == -1 { return -1 }
        if math.Abs(float64(l-r)) > 1 { return -1 }
        return max(l,r) + 1
    }
    ret := dfs(root)
    return ret != -1
}

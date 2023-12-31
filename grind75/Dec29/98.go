/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    var dfs func(*TreeNode, int, int) bool

    dfs = func(root *TreeNode, maxv int, minv int) bool {
        if root == nil {
            return true
        }
        if root.Val >= maxv || root.Val <= minv {
            return false
        }
        l := dfs(root.Left, root.Val, minv)
        r := dfs(root.Right, maxv, root.Val)
        return l && r
    }

    return dfs(root.Left, root.Val, math.MinInt) && dfs(root.Right, math.MaxInt, root.Val)
}

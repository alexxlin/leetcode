/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
    ret := -1 
    var dfs func(*TreeNode) bool
    dfs = func(root *TreeNode) bool {
        if root == nil {
            return false
        }
        if dfs(root.Left) {
            return true
        }
        k--
        if k == 0 {
            ret = root.Val
            return true
        }
        if dfs(root.Right) {
            return true
        }
        return false
    }
    dfs(root)
    return ret
}

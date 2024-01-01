/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    ret := math.MinInt

    var dfs func(*TreeNode) int
    dfs = func(root *TreeNode) int {
        if root == nil {
            return 0
        }
        l := dfs(root.Left)
        r := dfs(root.Right)
        ret = max(ret, l+r)
        return max(l, r)+1
    }
    dfs(root)
    return ret
}

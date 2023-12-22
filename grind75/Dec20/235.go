/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	val, lval, rval := root.Val, p.Val, q.Val
    if val > lval && val > rval {
        return lowestCommonAncestor(root.Left, p, q)
    }
    if val < lval && val < rval {
        return lowestCommonAncestor(root.Right, p, q)
    }
    return root

}

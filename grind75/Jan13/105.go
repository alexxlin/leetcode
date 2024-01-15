/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 { return nil }
    val := preorder[0]
    root := &TreeNode{Val: val}
    idx := findIdx(inorder, val)
    root.Left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.Right = buildTree(preorder[idx+1:], inorder[idx+1:])
    return root
}

func findIdx(arr []int, val int) int {
    for i:= 0 ; i < len(arr); i++ {
        if arr[i] == val {
            return i
        }
    }
    return -1
}

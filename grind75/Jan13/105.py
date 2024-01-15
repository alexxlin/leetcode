# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> 
Optional[TreeNode]:
        if inorder:
            root = preorder.pop(0)
            root_index = inorder.index(root)
            left = inorder[:root_index]
            right = inorder[root_index+1:]
            root_node = TreeNode(root)
            root_node.left = self.buildTree(preorder, left)
            root_node.right = self.buildTree(preorder, right)
            return root_node

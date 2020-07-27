# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        
        #inorder traversal in a BST will be increasing
        #time: O(n)
        #space: O(1)
        
        minimum = 100
        previous = -100
        def recursive(node):
            
            nonlocal minimum
            nonlocal previous
            
            if node:
                recursive(node.left)
                
                minimum = min(node.val - previous, minimum)
                previous = node.val
                
                recursive(node.right)
            
        recursive(root)
        return minimum
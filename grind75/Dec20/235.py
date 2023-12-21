# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 
'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root

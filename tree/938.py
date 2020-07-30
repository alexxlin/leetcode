# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        #recursive inorder
        
        #time: O(n) visting all nodes
        #space: O(h) at most h recursive stacks (keep going node.left, then exiting recursive stack)
        
        
        sum = 0
        
        def inorder(node):
            
            nonlocal sum
            
            if node:
                inorder(node.left)
                
                if L <= node.val <= R:
                    sum += node.val
                    
                inorder(node.right)
                
        inorder(root)
        return sum
                    
                
                    
                
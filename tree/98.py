# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        #inorder traversal
        
        #time: O(n)
        #space: O(1)
        
        if root == None:
            return True
        
        previous = - math.inf
        valid = True
        
        def recursive(node):
        
        
            if node:
                recursive(node.left)
                
                if node.val <= previous:
                    valid = False
                previous = node.val
                
                recursive(node.right)
                
       
        recursive(root)
        return valid
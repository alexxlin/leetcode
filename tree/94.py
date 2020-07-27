# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        #use a stack to store the nodes
        
        #time: O(n)
        #space: O(n)
        
        #basecase
        if not root:
            return []
        
        stack = []
        result = []

        
        while stack or root:
            
            if root:
                stack.append(root)
                root = root.left
            
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
                
                    
        return result
                
            
            
            
            
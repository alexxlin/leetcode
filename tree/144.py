# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        #time: O(n)
        #space: O(n)
        
        stack = [root]
        result = []
        
        while stack:
            
            node = stack.pop()
            if node:
                result.append(node.val)

                stack.append(node.right)
                stack.append(node.left)
        
        return result
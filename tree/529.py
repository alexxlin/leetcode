"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        #method 1: recursion
        
#         #time: O(n)
#         #space: O(1)
        
#         result = []
        
#         def recursive(node):
            
#             if node:
                
#                 for child in node.children:
#                     recursive(child)
                
#                 result.append(node.val)
        
#         recursive(root)
#         return result

        #method 2: iterative
        
        if root == None:
            return None
        
        stack = [root]
        result = []
        
        while stack:
            
            root = stack.pop()
            
            result.append(root.val)
            
            if root.children:
                
                for child in root.children:
                    stack.append(child)
                
                
        
        return result[::-1]
        
                
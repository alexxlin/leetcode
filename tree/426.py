"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        #inorder travel will sort all nodes
        
        #time: O(n)
        #space: O(1)
        
        #basecase
        if not root:
            return root
        
        self.last = None
        self.first = None
        
        def inorder(node):
            
            if node:
                
                inorder(node.left)
                
                if not self.first:
                    self.first = node
                
                if self.last:
                    self.last.right = node
                    node.left = self.last
                
                self.last = node
                
                inorder(node.right)
                self.last.right = self.first
                self.first.left = self.last
                
        inorder(root)
        return self.first
                    
            
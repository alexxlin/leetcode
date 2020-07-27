# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        #recursive
        def invert(node):
            
            if node == None:
                return
            
            if node.left == None and node.right == None:
                return

            if node.left != None and node.right == None:
                node.right = node.left
                node.left = None


            elif node.right != None and node.left == None:
                node.left = node.right
                node.right = None

            else:            
                temp = node.left
                node.left = node.right
                node.right = temp
            
            invert(node.left)
            invert(node.right)
        
        invert(root)
        return root
        
        
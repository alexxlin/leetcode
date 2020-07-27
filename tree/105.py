# Definition for a binary tree node.
# class TreeNode
#     def __init__(self, val=0, left=None, right=None)
#         self.val = val
#         self.left = left
#         self.right = right
class Solution
    def buildTree(self, preorder List[int], inorder List[int]) - TreeNode
        
        #in preoder, first node is root
        #in inorder, left of root is left subtree, right of root is right subtree
        
        if inorder
        
            root = preorder.pop(0)
            root_i = inorder.index(root)
            root_node = TreeNode(root)

            left = inorder[root_i]
            right = inorder[root_i + 1]

            root_node.left = self.buildTree(preorder, left)
            root_node.right = self.buildTree(preorder, right)

            return root_node
    
        
        
        
        
               
            
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        
        #if deleted is a leaf, just delete it
        #if deleted is a parent, its children become forest
        #order of traversal doesn't matter
        
        #time: O(n)
        #space: O(n) if all the second-last level are deleted, all leafs will be appended
        
        def postOrder(node, to_delete):
            
            if node != None:
            
                postOrder(node.left, to_delete)
                postOrder(node.right, to_delete)
                
                #if a child is to delete, then delete to pointer from its parent to it
                #and set it's child as roots of forest to be appended to result
                if node.left != None and node.left.val in to_delete:
                    
                    
                    if node.left.left != None:
                        result.append(node.left.left)
                    
                    if node.left.right != None:
                        result.append(node.left.right)
                                        
                    node.left = None
                
                if node.right != None and node.right.val in to_delete:
                    
                    
                    if node.right.left != None:
                        result.append(node.right.left)
                    
                    if node.right.right != None:
                        result.append(node.right.right)
                                        
                    node.right = None
                
        #basecase
        if root.val == None:
            return root
        
        result = []
        
        #the root node needs to be considered separately
        if root.val not in to_delete:
            result.append(root)
        
        else:
            if root.left != None and root.left.val not in to_delete:
                result.append(root.left)
            if root.right != None and root.right.val not in to_delete:
                result.append(root.right)
        
        
        postOrder(root, to_delete)      
        
        return result
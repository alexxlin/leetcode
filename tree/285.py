# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        #method 1, inorder traversal
        
#         #time: O(n)
#         #space: O(1)
        
#         #basecase
#         if root == None:
#             return root
        
#         found_p = False
#         result = None
        
#         def recursive_inorder(node, p):
            
#             nonlocal found_p
#             nonlocal result
            
#             #after we have found p, store the next node into result and return it
#             if node:
                
#                 recursive_inorder(node.left, p)

#                 if found_p:
#                     result = node
#                     found_p = False
                
#                 if node == p:
#                     found_p = True


#                 recursive_inorder(node.right, p)
                
#         recursive_inorder(root, p)
#         return result

        #method 2 (very elegant solution):
        #in binary tree, the sucessor of a node would be the smallest node larger than it
        #for a node, if it is smaller than p, it can't be a successor
        #if it is larger than p, it can be successor, but we want to find a smallest
        #node that is still larger than p, thus keep going left
        
        
        #time: O(h)
        #space: O(1)
        
        value = p.val
        node = root
        sucessor = None
        
        while node:
                
            #two scenarios, node is higher than p, going left would reach p
            #or node is in left subtree of p, going left would reach the smallest
            #node larger than p
            if node.val > value:
                sucessor = node
                node = node.left
            
            #two scenarios, node is higher than p, going left would reach p
            #when reaching p, go right once so that it is larger than p
            else:
                node = node.right
        
        return sucessor
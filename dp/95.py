# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        #similar concept to #96
        #this DOESN'T WORK because I  couldn't build a 
        #helper function to deep copy a tree while
        #adding a constant value to all nodes
        
        #helper function, create a new tree using old tree
        #while adding a constant to every node
#         def copy_tree(root, new, constant):
            
#             if root:
                
#                 copy_tree(root.left, new.left, constant)
                
#                 if new:
#                     print(type(new))
#                     if new.right:
#                         print(new.right.val)
#                     new.val = root.val + constant
#                     print(type(new))
#                     if new.right:
#                         print(new.right.val)
                
#                 copy_tree(root.right, new.right, constant)
                
#             return new
        
#         dp = [[] for i in range(n + 1)]
        
#         dp[0].append(None)
        
#         dp[1].append(TreeNode(1))
        
#         #populating dp for each i
#         for i in range(2, n+1):
            
#             #computing the BST with j being the root
#             for j in range(1, i + 1):
                
#                 for left_sub in dp[j - 1]:
#                     temp = TreeNode(j)
#                     temp.left = left_sub
                    
#                     for right_sub in dp[i - j]:
#                         if right_sub:
#                             new_tree = TreeNode(right_sub)
#                             new_tree = copy_tree(right_sub, new_tree, j)
#                             temp.right = new_tree
#                         dp[i].append(temp)
        
#         return dp[n]

        #recursive with memo
    
        #time: O(n ** 3)?
        #space: O(n ** 2)?

        if n == 0:
            return []
        
        memo = {}
        def recursive(first, last):
            
            if (first, last) in memo:
                return memo[(first, last)]
            
            result = []
            for root in range(first, last + 1):
                for left in recursive(first, root - 1):
                    for right in recursive(root + 1, last):
                        result.append(TreeNode(root, left, right))
            
            memo[(first, last)] = result if result else [None]
            return memo[(first, last)]
        
        return recursive(1, n)
        
        
        #dp bottom up
        #dp[i][j] gives all BSTs for values between i and j 
        #no dp-related discussions, I give up
        
#         dp = [[None for j in range(n + 1)] for i in range(n + 1)]
        
#         for i in range(1, n + 1):
#             dp[i][i] = [TreeNode(i)]
        
        
        
        
        
            
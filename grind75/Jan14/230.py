# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> 
int:
        # inorder traversal iteratively
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                root = node.right

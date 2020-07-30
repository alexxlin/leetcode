# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        #for each layer, return right most node
        #use breath first search
        
        #time: O(n)
        #space: O(n)
        
        if not root:
            return root
        
        result = []
        stack = [root]
        
        while stack:
            
            children = []
            while stack:
                right_node = stack.pop()
                children.append(right_node)
            
            result.append(right_node.val)
                
            for i in range(-1, -len(children) - 1, -1):
                if children[i].right:
                    stack.append(children[i].right)
                if children[i].left:
                    stack.append(children[i].left)
        
        return result
        
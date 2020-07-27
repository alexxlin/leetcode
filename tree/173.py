# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    
    #next smallest, use inorder
    #use stack structure
    #invariant: the element on top of stack is always the next smallest
    
    
    
    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorder_left(root)
        
    #first populate the stack with the left most path only
    def inorder_left(self, root):
        
        while root:
            self.stack.append(root)
            root = root.left

    
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        #result is of type TreeNode
        result = self.stack.pop(-1)
        
        #when popping the smallest item, if it has a right child, that call the helper
        #function on the right child
        #this way we don't miss any node
        
        
        if result.right:
            self.inorder_left(result.right)
        
        return result.val
            
        
        
        
        
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        #time: O(n)
        #space: O(n)
        
        #method 1: level-order traversal (BFS) (queue)
        
#         queue = []
        
#         queue.append(root)
        
#         while queue:
            
#             node = queue.pop(0)
            
#             print(node.val)
            
#             if len(queue) % 2 == 0:
#                 node.next = None
#             else:
#                 node.next = queue[0]
            
#             if (node.left != None):
#                 queue.append(node.left)
#                 queue.append(node.right)

        #method 2: node.right.next = node.next.left
        #at each level, setup next pointers in its children (in the next level)

        #time: O(n) setting up next pointer for (almost) all nodes
        #space: O(1) no extra space used to store queues
        
        
        #basecase, empty tree
        if not root:
            return root
        
        #if given node has children
        if root.left != None:
            root.left.next = root.right   
        
            #if given node is not the rightmost node of the level
            if root.next != None:
                root.right.next = root.next.left
        
            #recursive for its children
            self.connect(root.left)
            self.connect(root.right)
            
            
        return root
        
        
        
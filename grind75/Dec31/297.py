# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # using a preorder traversal
    # 
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/394234/python-preorder/

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            nonlocal traversal
            if not root:
                traversal += '#' + ' '
                return
            traversal += str(root.val) + ' '
            preorder(root.left)
            preorder(root.right)
        traversal = ''
        preorder(root)
        return traversal

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(' ')
        return self.helper(data_list)

    def helper(self, data_list):
        if data_list[0] == '#':
            data_list.pop(0)
            return

        root = TreeNode(data_list[0])
        data_list.pop(0)
        root.left = self.helper(data_list)
        root.right = self.helper(data_list)
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

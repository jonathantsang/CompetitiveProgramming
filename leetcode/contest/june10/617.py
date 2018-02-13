# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def recurse(self, node1, node2):
        # Same placed nodes
        if(node1.left and node2.left):
            self.recurse(node1.left, node2.left)
        node1.val += node2.val
        if(node1.right and node2.right):
            self.recurse(node1.right, node2.right)
        
        # node2 has it but not node1
        if(node2.left and node1.left == None):
            node1.left = TreeNode(0)
            self.recurse(node1.left, node2.left)
        if(node2.right and node1.right == None):
            node1.right = TreeNode(0)
            self.recurse(node1.right, node2.right)
            
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if(t1 == None):
            return t2
        if(t2 == None):
            return t1
        self.recurse(t1, t2)
        return t1
        
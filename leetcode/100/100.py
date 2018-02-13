# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def recurseTree(self, node1, node2):
        if(node1 == None and node2 == None):
            return True
        if(node1 == None or node2 == None):
            return False
        elif(node1.val == node2.val):
            return True and self.recurseTree(node1.left, node2.left) and self.recurseTree(node1.right, node2.right)
        else:
            return False
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.recurseTree(p, q)
        
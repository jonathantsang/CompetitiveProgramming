# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    self.largestBranch = 0
    
    def recurseTree(self, root):
        if(root == None):
            return 0
        else:
            left = self.recurseTree(root.left)
            right = self.recurseTree(root.right)
            return 1 + max(, )
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        left = self.recurseTree(root.left)
        right = self.recurseTree(root.right)
        if(largestBranch > min(left, right)):
            return largestBranch + max(left, right)
        else:
            ## This is for going through the root
            return 1 + left + right
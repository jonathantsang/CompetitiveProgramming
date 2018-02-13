# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        if(root.left != None):
            if(root.left.left == None and root.left.right == None):
                return root.left.val + Solution.sumOfLeftLeaves(self, root.left) + Solution.sumOfLeftLeaves(self, root.right)
            else:
                return Solution.sumOfLeftLeaves(self, root.left) + Solution.sumOfLeftLeaves(self, root.right)
        else:
            return Solution.sumOfLeftLeaves(self, root.left) + Solution.sumOfLeftLeaves(self, root.right)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def recurse(self, node, res):
        if(node):
            self.recurse(node.left, res)
            res.append(node.val)
            self.recurse(node.right, res)
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        self.recurse(root, inorder)
        return inorder
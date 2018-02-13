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
            self.recurse(node.right, res)
            res.append(node.val)
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        post = []
        self.recurse(root, post)
        return post
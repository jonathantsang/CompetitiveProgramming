# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    greater = 0
    
    def recurseBST(self, node):
        if(node):
            self.recurseBST(node.right)
            save = node.val
            node.val += self.greater
            self.greater += save
            self.recurseBST(node.left)


    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.greater = 0
        self.recurseBST(root);
        return root
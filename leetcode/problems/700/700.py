# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        def traverse(node, val):
            if node:
                if val == node.val:
                    return node
                if val > node.val:
                    return traverse(node.right, val)
                else:
                    return traverse(node.left, val)
            return None
        
        return traverse(root, val)
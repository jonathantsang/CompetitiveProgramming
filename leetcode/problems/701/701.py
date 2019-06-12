# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while True:
            # Right
            if node.val < val:
                if node.right == None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
# traverse the tree
# left smaller than current, right larger than current
# at the leaf node, put it based on the leaf value
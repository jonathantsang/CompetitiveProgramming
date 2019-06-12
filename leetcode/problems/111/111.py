# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node, amt):
            if node:
                if node.left == None and node.right == None:
                    return amt
                else:
                    return min(traverse(node.left, amt+1), traverse(node.right, amt+1))
            return 99999
                    
                
        if root == None:
            return 0
        return traverse(root, 1)
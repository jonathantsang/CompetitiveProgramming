# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        previous = None
        node = TreeNode(s[0])
        for char in s:
            if(type(char) == type(1)):
                node = TreeNode(char)
            elif(char == "(")
            
            else:
                node = previous
class Solution:
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    output = ""
    
    def preorder(self, node):
        if(node):
                self.output += str(node.val)
                if(node.left == None and node.right != None):
                    self.output += "()"
                elif(node.left != None):
                    self.output += "("
                    self.preorder(node.left)
                    self.output += ")"
                if(node.right != None):
                    self.output += "("
                    self.preorder(node.right)
                    self.output += ")"
                
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.output = ""
        self.preorder(t)
        return self.output
        
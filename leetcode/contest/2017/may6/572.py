# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def checkTree(self, nodeS, nodeT):
        if(nodeS == None and nodeT == None):
            return True
        elif(nodeS == None or nodeT == None):
            return False
        elif(nodeS.val == nodeT.val):
            print(str(nodeS.val) + " " + str(nodeT.val))
            return self.checkTree(nodeS.left, nodeT.left) and self.checkTree(nodeS.right, nodeT.right)
        else:
            return False
    
    ## This will check to see if the root node is in the tree, and check from there
    def recurseTree(self, node, findVal, t):
        if(node):
            ## Check the value to see if it is the correct node
            if(node.val == findVal):
                print("check")
                val = self.checkTree(node, t)
                print(val)
                if(val == True):
                    return True
            ## Else recurse on the rest of the tree
            return self.recurseTree(node.left, findVal, t) or self.recurseTree(node.right, findVal, t)
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        findVal = t.val
        done = self.recurseTree(s, findVal, t)
        if(done == None):
            return False
        return True
        
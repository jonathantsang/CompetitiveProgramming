# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def iterateTree(self, node, fullString):
        current = node
        s = [] # initialze stack
        done = 0
        while(not done):
            if current is not None:
                s.append(current)
                current = current.left 
            else:
                if(len(s) >0):
                    current = s.pop()
                    fullString += str(current.val)
                    current = current.right 
                else:
                    done = 1
                    return fullString
        
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        full = self.iterateTree(s, "")
        subtree = self.iterateTree(t, "")
        print(full)
        print(subtree)
        valid = True
        for i in range(0, len(full)):
            if(full[0] == subtree[0]):
                ## Check if the substring is the valid subtree
                for j in range(1, len(subtree)):
                    if(full[j] != subtree[j]):
                        valid = False
                        break
                if(valid == True):
                    return True
        return False
        
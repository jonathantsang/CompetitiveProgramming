# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ht = dict();
    
    def recurseTree(self, node):
        if(node):
            self.recurseTree(node.left)
            self.recurseTree(node.right)
            if(node.val in self.ht):
                self.ht[node.val] += 1
            else:
                self.ht[node.val] = 1

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root == None):
            return []
        self.ht = dict();
        self.recurseTree(root)
        maxl = []
        max_ct = max(self.ht.itervalues())
        for k in self.ht.keys():
            if(self.ht[k] == max_ct):
                maxl.append(k)
        return maxl
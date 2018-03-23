# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    arr = []
    def runArr(self, arr):
        leng = len(arr)
        min = abs(arr[0] - arr[1])
        for i in range(1, leng):
            diff = abs(arr[i] - arr[i - 1])
            if(diff < min):
                min = diff
        return min
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.arr = []
        self.recurse(root)
        print(self.arr)
        return self.runArr(self.arr)
        
    def recurse(self, root):
        if(root):
            if(root.left != None):
                self.recurse(root.left)
                self.arr.append(root.val)
                self.recurse(root.right)
            else:
                self.arr.append(root.val)
                self.recurse(root.right)

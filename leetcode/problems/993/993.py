# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, cur, lookfor, parent, depth):
        if cur:
            if cur.val == lookfor:
                return parent, depth
            a, b = self.search(cur.left, lookfor, cur, depth+1)
            if a != None and b != None:
                return a, b
            c, d = self.search(cur.right, lookfor, cur, depth+1)
            if c != None and d != None:
                return c, d
        return None, None
            
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        xparent, xdepth = self.search(root, x, None, 0)
        yparent, ydepth = self.search(root, y, None, 0)
        if xdepth == ydepth and xparent != yparent:
            return True
        return False
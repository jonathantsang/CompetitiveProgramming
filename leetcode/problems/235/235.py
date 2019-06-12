# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    parent = {} # Key: node, Value: Parent TreeNode
    
    def traverse(self, node, prev):
        if node:
            self.parent[node] = prev
            self.traverse(node.left, node)
            self.traverse(node.right, node)
            
    def level(self, node, val, count):
        if node:
            if node == val:
                return count
            a = self.level(node.left, val, count+1)
            if a != -1:
                return a
            b = self.level(node.right, val, count+1)
            if b != -1:
                return b
        return -1

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parent = {}
        self.traverse(root, None)
        anc = root
        plevel = self.level(root, p, 0)
        qlevel = self.level(root, q, 0)
        #print(self.parent)
        #print(plevel, qlevel)
        if plevel < qlevel:
            p, q = q, p
            plevel, qlevel = qlevel, plevel
        while plevel > qlevel:
            p = self.parent[p]
            plevel -= 1
        while p != q:
            # print(p.val, q.val)
            if p == root or q == root:
                return root
            p = self.parent[p]
            q = self.parent[q]
            plevel -= 1
            qlevel -= 1
        return p
        
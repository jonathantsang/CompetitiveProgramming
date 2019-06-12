# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    depths = {}
    def traverse(self, node, depth):
        if node:
            if depth not in self.depths:
                self.depths[depth] = node.val
            self.traverse(node.right, depth+1)
            self.traverse(node.left, depth+1)
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.depths = {} # Key: depth -> id of node
        ans = []
        self.traverse(root, 0)
        for depth in self.depths:
            while depth >= len(ans):
                ans.append(0)
            ans[depth] = self.depths[depth]
        return ans
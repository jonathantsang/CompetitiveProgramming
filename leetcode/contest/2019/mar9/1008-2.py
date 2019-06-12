# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct(self, current, valuetobeadded):
        if current:
            # Left side
            if current.val > valuetobeadded:
                if current.left == None:
                    current.left = TreeNode(valuetobeadded)
                else:
                    self.construct(current.left, valuetobeadded)
            # Right size
            else:
                if current.right == None:
                    current.right = TreeNode(valuetobeadded)
                else:
                    self.construct(current.right, valuetobeadded)
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index = 1
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.construct(root, preorder[i])
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        
        def traverse(node: 'TreeNode') -> 'str':
            if node:
                if node.left == None and node.right == None:
                    return chr(node.val + 97)
                else:
                    v = min(traverse(node.left), traverse(node.right))
                    return v + chr(node.val + 97)
            return chr(128)
        
        string = str(root.val)
        if root.left == None and root.right == None:
            return chr(root.val + 97)
        
        value = min(traverse(root.left), traverse(root.right)) +  chr(root.val + 97)
        # print(value)
        return value
            
        
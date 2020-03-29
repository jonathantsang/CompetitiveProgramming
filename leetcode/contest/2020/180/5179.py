# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct(self, prev, rest):
        if len(rest) == 0:
            return
        mid = len(rest) // 2
        new_node = TreeNode(rest[mid])
        if rest[mid] < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node
        self.construct(new_node, rest[:mid])
        self.construct(new_node, rest[mid+1:])
            
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        queue = [root]
        while len(queue) > 0:
            val = queue.pop()
            nodes.append(val.val)
            if val.left != None:
                queue.append(val.left)
            if val.right != None:
                queue.append(val.right)
        nodes.sort()
        # divide and conquer
        mid = len(nodes) // 2
        start = TreeNode(nodes[mid])
        self.construct(start, nodes[:mid])
        self.construct(start, nodes[mid+1:])
        return start
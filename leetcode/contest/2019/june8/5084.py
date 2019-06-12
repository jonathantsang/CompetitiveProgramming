# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    delete = [] # Nodes to delete
    def traverse(self, node, cur, limit):
        # print(node.val, cur)
        if node:
            # Check if leaf
            if node.left == None and node.right == None:
                return (cur+node.val) >= limit # True not insufficient, False is insufficient
            
            # Check children
            a = self.traverse(node.left, cur+node.val, limit) if node.left != None else False
            b = self.traverse(node.right, cur+node.val, limit) if node.right != None else False
            
            if a == False and b == False: # Both fail
                # Remove from the tree
                self.delete.append([node, "right"])
                self.delete.append([node, "left"])
                return False
            else:
                if a == False:
                    self.delete.append([node, "left"])
                elif b == False:
                    self.delete.append([node, "right"])
                return True
        return True
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        res = self.traverse(root, 0, limit)
        if res == False:
            return None
        for p in self.delete:
            if p[0] == None:
                continue
            if p[1] == "left":
                p[0].left = None
            else:
                p[0].right = None
        return root
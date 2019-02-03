# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    parents = {} # key is TreeNode, value: TreeNode that is the parent
    moves = 0
    def traverse(self, node):
        if (node):
            if node.left != None:
                self.parents[node.left] = node
            if node.right != None:
                self.parents[node.right] = node
            self.traverse(node.left)
            self.traverse(node.right)
            
    def fill(self, node):
        if (node):
            if (node.val == 0):
                self.moves += self.findspare(node, node, {}, 0)
            # Go to children afterwards
            self.fill(node.left)
            self.fill(node.right)
            
    def findspare(self, node, curnode, seen, travelled):
        # print("find spare")
        # Found spare already
        if node.val == 1:
            return 999
        
        if curnode in seen and seen[curnode] < travelled:
            return 999
        else:
            seen[curnode] = travelled
            
        # Move upwards and two ways downwards to find a spare coin node
        if (curnode):
            if curnode.val > 1:
                curnode.val -= 1
                node.val += 1
                # self.moves += travelled
                return travelled
            else:
                lef = self.findspare(node, curnode.left, seen, travelled + 1)
                rig = self.findspare(node, curnode.right, seen, travelled + 1)
                up = 999
                # find parent
                if curnode in self.parents:
                    up = self.findspare(node, self.parents[curnode], seen, travelled + 1)
                return min(lef, rig, up)
        return 999
        
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        self.fill(root)
        return self.moves
        
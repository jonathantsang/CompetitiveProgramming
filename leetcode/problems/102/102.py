# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root, None]
        levels = [[]]
        while len(queue) != 0:
            # print(queue)
            val = queue[0]
            if val == None:
                if levels[len(levels)-1] == []:
                    levels = levels[:len(levels)-1]
                    break
                levels.append([])
                queue.append(None)
                queue = queue[1:]
                continue
            levels[len(levels)-1].append(val.val)
            
            if val.left != None:
                queue.append(val.left)
            if val.right != None:
                queue.append(val.right)
            queue = queue[1:]
        return levels
            
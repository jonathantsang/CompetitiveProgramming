from collections import defaultdict

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        lefts = defaultdict(list) # number offset from left -> values

        def dfs(node, l):
            if node:
                lefts[l].append(node.val)
                dfs(node.left,l+1)
                dfs(node.right,l)

        dfs(root,0)

        i = 0
        ans = []
        while i in lefts:
            ans.append(sum(lefts[i]))
            i+=1
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:

        ans = 0
        def palCheck(vals):
            #print(vals)
            # can only have at most 1 odd amt
            odd = 0
            for v in vals:
                if vals[v] & 1 == 1:
                    odd += 1
                    if odd > 1:
                        return False
            return True

        def dfs(node, vals):
            nonlocal ans
            if node:
                vals[node.val] += 1
                # leaf
                if node.left == None and node.right == None:
                    # check if values in val can construct palindrome
                    if palCheck(vals):
                        ans += 1
                else:
                    dfs(node.left, vals)
                    dfs(node.right, vals)
                vals[node.val] -= 1

        start = collections.defaultdict(int)
        dfs(root, start)

        return ans

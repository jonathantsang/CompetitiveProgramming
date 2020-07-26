# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        pairs = 0
        def dfs(node): # pass up dictionary of how many nodes at each distance?
            nonlocal pairs
            if node:
                dists = Counter()
                # leaf
                if node.left == None and node.right == None:
                    dists[node] = 0
                    return dists
                else:
                    a = dfs(node.left)
                    b = dfs(node.right)

                    for child_leaf in a:
                        a[child_leaf] += 1
                    for child_leaf in b:
                        b[child_leaf] += 1

                    for cl1 in a:
                        for cl2 in b:
                            if a[cl1] + b[cl2] <= distance:
                                pairs += 1
                    return a + b

            return Counter()

        dfs(root)
        return pairs

            

from collections import defaultdict, deque

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        leaves = defaultdict(int) # node # -> depth for leaves

        q = deque([(root, 0, "")])
        while q:
            node, d, part = q.popleft()

            if node.left:
                q.append((node.left, d+1, part + str(node.val)))
            if node.right:
                q.append((node.right, d+1, part + str(node.val)))

            if node.left == None and node.right == None:
                leaves[part] = d

        # get second highest value
        m1 = -1
        m2 = -1
        for l in leaves:
            if leaves[l] > m1:
                m2 = m1
                m1 = leaves[l]
            elif leaves[l] > m2:
                m2 = leaves[l]

        return m2

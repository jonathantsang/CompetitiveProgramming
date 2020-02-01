# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        import collections
        
        ans = []
        queue = collections.deque()
        queue.append(root)
        while(len(queue) > 0):
            node = queue.popleft()
            if node == None:
                continue
            ans.append(node.val)
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        return ans
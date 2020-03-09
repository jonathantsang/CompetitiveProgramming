# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, node, llnode, started):
        if llnode == None:
            return True
        elif node:
            a = False
            if node.left and node.left.val == llnode.val:
                a = self.check(node.left, llnode.next, True)
            if a:
                return a
            if node.right and node.right.val == llnode.val:
                a = self.check(node.right, llnode.next, True)
            if a:
                return a
            
            # Cut off search
            if started:
                return False
            else:
                return self.check(node.left, llnode, False) or self.check(node.right, llnode, False)
        return False
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        starter = TreeNode(-1)
        starter.right = root
        return self.check(starter, head, False)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def recurse(self, node):
        if node:
            end = self.recurse(node.next)
            if not end:
                return end
            elif self.temp.val == node.val:
                return True
            else:
                return False
        return True
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.temp = head
        return self.recurse(head)
        
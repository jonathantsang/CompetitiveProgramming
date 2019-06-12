# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        node = head
        prev = None
        cur = node
        while cur != None and cur.val == val:
            cur = cur.next
        node = cur
        if cur == None:
            return None
            
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
            
        return node
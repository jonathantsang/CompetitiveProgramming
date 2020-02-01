# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
        # p1 is shorter
        if p2 == None:
            p1, p2 = p2, p1
            headA, headB = headB, headA
        
        adj = 0
        while p2 != None:
            p2 = p2.next
            adj += 1
            
        # New run with adj
        p1 = headA
        p2 = headB
        
        for i in range(0, adj):
            p2 = p2.next
        while p1 != None and p2 != None:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
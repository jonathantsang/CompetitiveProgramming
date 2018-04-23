# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        head = new = ListNode(0)
        while(l1 != None or l2 != None):
            if(l1 == None):
                new.next = l2
                l2 = l2.next
            elif(l2 == None):
                new.next = l1
                l1 = l1.next
            elif(l1.val < l2.val):
                new.next = l1
                l1 = l1.next
            elif(l2.val <= l1.val):
                new.next = l2
                l2 = l2.next
            new = new.next
        return head.next
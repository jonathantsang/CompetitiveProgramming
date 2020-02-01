# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(0, n+1):
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
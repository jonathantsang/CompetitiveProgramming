# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        self.nextval(node, head)
        
        
    def nextval(self, node, previous):
        if(node.next != None):
            self.nextval(node.next, node)
            while(node.next != None and node > node.next):
                previous.next = node.next
                node.next = node
                previous = previous.next
        
            
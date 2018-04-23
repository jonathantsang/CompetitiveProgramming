# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def valorzero(self, node):
        if(node == None):
            return 0
        else:
            return node.val
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        ## Check if they are 
        if(l1 != None or l2 != None):
            ## Calc val
            total = self.valorzero(l1) + self.valorzero(l2)
            head.val = total % 10
            head.next = None
            carry = total // 10
        else:
            return None
        newnode = head
        ## Increment because beginning edge case
        l1 = l1.next
        l2 = l2.next
        while(l1 != None or l2 != None or carry > 0):
            ## Oldnode is the previous one
            oldnode = newnode
            ## New node is made
            newnode = ListNode(0)
            ## The next of the old one is the new one
            oldnode.next = newnode
            ## Calc val
            if(l1 == None and l2 == None):
                ## Special case where only carry is > 0
                newnode.val = carry
                return first
            else:
                total = self.valorzero(l1) + self.valorzero(l2) + carry
                newnode.val = total % 10
                carry = total // 10
                ## Set the new node to point at end
                newnode.next = None
                ## Increment LL if possible
                if(l1 != None):
                    l1 = l1.next
                if(l2 != None):
                    l2 = l2.next
        return first
        
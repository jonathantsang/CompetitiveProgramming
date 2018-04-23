# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len = 1
        first = head
        counter = k
        if(head == None):
            return []
        if(k == 0):
            return head
        ## Make the LL a circle
        while(head.next != None):
            head = head.next
            len = len + 1
        ## Reduce k to lowest value
        k = k % len
        ## Find the first node of the LL
        start = abs(len - k)
        ind = 0
        ## Case where start is 0, meaning the array is unrotated
        if(start == 0):
            return first
        else:
             ## link the last node to the first
            head.next = first
            ## Start searching from the front again
            head = head.next
            ## Go through the LL to find the start point based on the length
            while(ind < start - 1):
                head = head.next
                ind = ind + 1
            ## Save the next as the starting node
            save = head.next
            ## End the LL at the node
            head.next = None
            ## Start is the saved node
            head = save
            return head
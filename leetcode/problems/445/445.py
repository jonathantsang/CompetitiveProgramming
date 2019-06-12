# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        oneleng = 0
        pt = l1
        while(pt != None):
            pt = pt.next
            oneleng += 1
        twoleng = 0
        pt = l2
        while(pt != None):
            pt = pt.next
            twoleng += 1
        ans = 0
        while(oneleng != twoleng):
            if oneleng > twoleng:
                ans *= 10
                ans += l1.val
                l1 = l1.next
                oneleng -= 1
            else:
                ans *= 10
                ans += l2.val
                l2 = l2.next
                twoleng -= 1
        while(oneleng > 0):
            ans *= 10
            ans += (l1.val + l2.val)
            oneleng -= 1
            twoleng -= 1
            l1 = l1.next
            l2 = l2.next
            
        a = None
        f = a
        for digit in str(ans):
            if a == None:
                a = ListNode(int(digit))
                a.next = None
                f = a
            else:
                b = ListNode(int(digit))
                a.next = b
                a = b
        return f
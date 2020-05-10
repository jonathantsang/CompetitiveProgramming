# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        # Write your code here
        fast = node
        slow = node
        vals = [slow.val]
        j = 0
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            vals.append(slow.val)
            j += 2
            
        if fast != None:
            j += 1
        vals.pop() # pop last one is midpoint?
        head = slow
        
        # slow is now mid
        i = len(vals)-1
        if j % 2 == 1:
            slow = slow.next # skip on odd fold over
        while slow != None:
            slow.val += vals[i]
            slow = slow.next
            i -= 1
        return head
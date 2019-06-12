class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        carry = 0
        a = 0
        for i in range(0, len(A)):
            a *= 10
            a += A[i]
        # print(a)
        a += K
        ans = []
        a = str(a)
        for d in a:
            ans.append(int(d))
        return ans
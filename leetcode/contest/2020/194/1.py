class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = [start+2*i for i in range(n)]
        a = ans[0]
        for i in range(1, n):
            a ^= ans[i]
        return a

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        vals = dict()
        for v in A:
            if v in vals:
                vals[v] += 1
            else:
                vals[v] = 1
        valid = 0
        A.sort()
        best = []
        print(vals)
        for i in range(0, len(A)):
            if vals[A[i]] == 0:
                continue # not valid
            if A[i] * 2 in vals and vals[A[i]*2] > 0:
                vals[A[i]*2] -= 1
                vals[A[i]] -= 1
                valid += 1
            print(vals)
            print(valid)
        return valid >= len(A) / 2
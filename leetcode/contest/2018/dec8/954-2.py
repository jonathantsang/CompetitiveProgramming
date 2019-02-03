class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        vals = dict()
        dpvals = dict()
        for v in A:
            if v in vals:
                vals[v] += 1
            else:
                vals[v] = 1
                dpvals[v] = 1
        valid = 0
        A.sort()
        best = 
        print(vals)
        # 0 to len(dpvals)
        i = 0
        for key in dpvals:
            if vals[A[i]] == 0:
                continue # not valid
            if A[i]*2 in vals and vals[A[i]*2] > 0:
                # limiting
                pairs = max(vals[A[i]*2], vals[A[i]])
                if i == 0:
                    best.append(max(best[i], pairs))
                else:
                    best.append(max(best[i], best[i-1] + pairs))
            i += 1
        return valid >= len(A) / 2
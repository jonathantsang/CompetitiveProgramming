class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        L, M = min(L, M), max(L, M)
        bestL = [0 for i in range(0, len(A))]
        bestM = [0 for i in range(0, len(A))]
        ans = 0
        bestL[L-1] = sum(A[:L])
        bestM[M-1] = sum(A[:M])

        for i in range(L, len(A)):
            bestL[i] = bestL[i-1] + A[i] - A[i-L]
        for i in range(M, len(A)):
            bestM[i] = bestM[i-1] + A[i] - A[i-M]
        #print(bestL)
        #print(bestM)
        
        # Find best pair of values that don't overlap
        for i in range(L-1, len(A)):
            for j in range(M-1, len(A)):
                # Check if overlapping
                # j-M <= i <= j
                # i-L <= j <= i
                if not ((j - M < i and i <= j) or (i - L < j and j <= i)):
                    ans = max(ans, bestL[i] + bestM[j])
                    # print(ans, bestL[i], bestM[j], i , j)
        return ans
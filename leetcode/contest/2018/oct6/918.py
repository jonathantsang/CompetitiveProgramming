class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        end = len(A)
        A.extend(A)
        cir = A
        ## print(cir)
        bestSum = -30001
        ## Perform on each n index
        for n in range(0, end):
            best = [cir[n]]
            j = 1
            for i in range(1+n, end+n):
                best.append(max(best[j-1]+cir[i], cir[i]))
                bestSum = max(bestSum, best[j])
                j += 1
        return bestSum
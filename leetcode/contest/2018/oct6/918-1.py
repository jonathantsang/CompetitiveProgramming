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
        
        bestSum = cir[0]
        best = [cir[0]]
        used = dict()
        cp = dict()
        cp[0] = 1
        used[0] = cp
        
        ## Perform on each n index
        for n in range(1, end):
            cp = cp.copy()
            value = max(best[n-1]+cir[n], cir[n])
            ## Restart index counts
            if (value == cir[n]):
                cp = dict()
            ## Add to the used dict
            cp[n] = 1
            used[n] = cp
            best.append(value)
        print(best)
        print(used)
        
        ## Altered ones
        for n in range(end, len(A)):
            ## Not used in the sum so proceed
            if (end - len(A)) not in used[n-1]:
                best.append(best[n-1]+cir[n], cir[n])
                cp = cp.copy()
                cp[end] = 1
                used[n] = cp
            ## Used in the optimal sum
            else:
                
        
        return bestSum
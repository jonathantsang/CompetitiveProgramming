class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        oddseq = False
        evenseq = False
        oddstart = 0
        oddend = 0
        evenstart = 0
        evenend = 0
        best = 0
        if len(A) == 1:
            return 1
        # Check up to 1 before end
        for i in range(0, len(A)-1):
            #print(i, "best", best)
            #print("odd", oddseq, oddstart, oddend)
            #print("even", evenseq, evenstart, evenend)
            # Even
            if i % 2 == 0:
                # even check < with i+1
                if A[i] < A[i+1]:
                    if not evenseq:
                        evenseq = True
                        evenend = i
                        evenstart = i
                        best = max(best, evenend - evenstart + 1) 
                    else:
                        evenend = i
                        best = max(best, evenend - evenstart + 1)
                else:
                    # End evenseq
                    if evenseq:
                        evenseq = False
                        evenend = i
                        best = max(best, evenend - evenstart + 1)
                        evenstart = evenend
                # odd check > with i+1
                if A[i] > A[i+1]:
                    if not oddseq:
                        oddseq = True
                        oddend = i
                        oddstart = i
                        best = max(best, oddend - oddstart + 1)
                    else:
                        oddend = i
                        best = max(best, oddend - oddstart + 1)
                else:
                    # End oddseq
                    if oddseq:
                        oddseq = False
                        oddend = i
                        best = max(best, oddend - oddstart + 1)
            # Odd
            else:
                # even check > with i+1
                if A[i] > A[i+1]:
                    if not evenseq:
                        evenseq = True
                        evenend = i
                        evenstart = i
                        best = max(best, evenend - evenstart + 1) 
                    else:
                        evenend = i
                        best = max(best, evenend - evenstart + 1)
                else:
                    # End evenseq
                    if evenseq:
                        evenseq = False
                        evenend = i
                        best = max(best, evenend - evenstart + 1)
                        evenstart = evenend
                
                # odd check < with i+1
                if A[i] < A[i+1]:
                    if not oddseq:
                        oddseq = True
                        oddend = i
                        oddstart = i
                        best = max(best, oddend - oddstart + 1)
                    else:
                        oddend = i
                        best = max(best, oddend - oddstart + 1)
                else:
                    # End oddseq
                    if oddseq:
                        oddseq = False
                        oddend = i
                        best = max(best, oddend - oddstart + 1)
                        oddstart = oddend
        # Ending
        if evenseq:
            evenend = len(A)-1
            best = max(best, evenend - evenstart + 1)
        elif oddseq:
            oddend = len(A)-1
            best = max(best, oddend - oddstart + 1)
        return best
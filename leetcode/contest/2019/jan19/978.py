class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lastT = 0
        firstT = 0
        firstF = 0
        lastF = 0
        seq = False
        best = 0
        if len(A) == 1:
            return 1
        # Check up to 1 before end
        for i in range(0, len(A)-1):
            print(i, "best", best)
            # Even, check < with i+1
            if i % 2 == 0:
                if A[i] < A[i+1]:
                    if not seq:
                        seq = True
                        firstT = i
                        lastT = i
                        
                        # Check last time
                        lastF = i
                        best = max(best, lastF - firstF + 1)
                        firstF = lastF
                    else:
                        lastT = i
                        best = max(best, lastT - firstT + 1)
                        # print("works so now best", best, lastT, firstT)
                # Failure of turbulent
                else:
                    if seq:
                        lastT = i
                        best = max(best, lastT - firstT + 1)
                        firstT = lastT
                        seq = False
                        firstF = i
                    else:
                        lastF = i
                        best = max(best, lastF - firstF + 1)
            # Odd, check > with i+1
            else:
                if A[i] > A[i+1]:
                    if not seq:
                        seq = True
                        firstT = i
                        lastT = i
                        
                        # Check last time
                        lastF = i
                        best = max(best, lastF - firstF + 1)
                        firstF = lastF                        
                    else:
                        lastT = i
                        best = max(best, lastT - firstT + 1)
                        # print("works so now best", best, lastT, firstT)
                else:
                    if seq:
                        lastT = i
                        best = max(best, lastT - firstT + 1)
                        firstT = lastT
                        seq = False
                        firstF = i
                    else:
                        lastF = i
                        best = max(best, lastF - firstF + 1)
                        
        # Afterwards

        return best
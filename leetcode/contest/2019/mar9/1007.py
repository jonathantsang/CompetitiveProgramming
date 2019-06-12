class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # Key = number, Value = array of set bits for index where it is valid
        ht = {}
        for i in range(1, 7):
            ht[i] = [0 for x in range(0, len(A))]
        for i in range(0, len(A)):
            ht[A[i]][i] |= 2
            ht[B[i]][i] |= 1
        minsteps = float('inf')
        for i in range(1, 7):
            if 0 in ht[i]:
                continue
            a = 0
            b = 0
            for v in ht[i]:
                if v & 1 == 1:
                    b += 1
                if v & 2 == 2:
                    a += 1
            minsteps = min(minsteps, len(A) - a, len(B) - b)
        return minsteps if minsteps != float('inf') else -1
        
        
        
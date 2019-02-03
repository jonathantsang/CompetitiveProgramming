class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ht = dict() # (sum, # of occurences)
        ht[0] = 1
        count = 0
        s = 0
        for i in range(0, len(A)):
            s += (A[i] % K)
            
            reverse = 4 - s % K
            if reverse in ht:
                count += ht[reverse]
            
            # Insert
            if s % K in ht:
                ht[s % K] += 1
            else:
                ht[s % K] = 1
            
        return count - 1
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        subarrays = 0
        for start in range(0, len(A)):
            val = 0
            for end in range(start, len(A)):
                val += A[end]
                if (val % K == 0):
                    subarrays += 1
        return subarrays
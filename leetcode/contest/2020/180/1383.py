class Solution:
    def maxPerformance(self, N, S, E, K): #n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        people = sorted(zip(E, S), reverse=True)
        ans = 0
        pq = []
        pqsum = 0
        for e, s in people:
            # now considering min effic is e
            heapq.heappush(pq, s)
            pqsum += s
            while len(pq) > K:
                pqsum -= heapq.heappop(pq)
            cand = pqsum * e
            ans = max(cand, ans)
            
        
        return ans % MOD
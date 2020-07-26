class Solution:
    def solve(self, nums0, nums1, dist, cost):
        N,M=len(nums0),len(nums1)
        MOD = 10**9+7

        dp1 = [float('inf') for _ in range(N)]
        dp2 = [float('inf') for _ in range(M)]
        dp1[0] = min(nums0[0],nums1[0]+cost)
        dp2[0] = min(nums1[0],nums0[0]+cost)

        for i in range(max(N,M)):
            if i < N and i < M:
                for j in range(max(i-dist,0),i):
                    # jump from dp1, jump from dp2 and incur cost
                    dp1[i] = min(dp1[i], dp1[j]+nums0[i], dp2[j]+nums1[i]+cost)

                    dp2[i] = min(dp2[i], dp2[j]+nums1[i], dp1[j]+nums0[i]+cost)
            elif i < N:
                for j in range(max(i-dist,0),i):
                    # jump from dp1, jump from dp2 and incur cost
                    dp1[i] = min(dp1[i], dp1[j]+nums0[i], dp2[j]+nums1[i]+cost)

            elif i < M:
                for j in range(max(i-dist,0),i):
                    # jump from dp1, jump from dp2 and incur cost
                    dp2[i] = min(dp2[i], dp2[j]+nums1[i], dp1[j]+nums0[i]+cost)
        return min(dp1[-1] % MOD, dp2[-1] % MOD)
        

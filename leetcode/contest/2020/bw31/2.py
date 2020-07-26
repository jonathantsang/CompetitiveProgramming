class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        N = len(arr)

        eo = [1,0]
        ssf = 0

        for i in range(N):
            ssf = ssf + arr[i]

            eo[ssf&1] +=1

        return (eo[0] * eo[1]) % MOD

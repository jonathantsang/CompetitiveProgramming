class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9+7
        ans = 0
        s = s.split('0')
        for v in s:
            leng = len(v)
            ans += leng # 1s
            for l in range(2,leng+1):
                # amount
                hi = l-1
                ans += leng - (hi)
        
        return ans % MOD
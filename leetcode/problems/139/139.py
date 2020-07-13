class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        dp = [False] * (N+1)
        words = set(wordDict)
        
        dp[0] = True
        
        for i in range(0, N+1):
            for j in range(i):
                substr = s[j:i]

                if dp[j] and substr in words:
                    dp[i] = True
                    break

        return dp[len(s)]
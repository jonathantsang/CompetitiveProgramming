class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)

        ans = []
        words = set(wordDict)
        
        def go(cons, part):
            if part in words:
                cons.append(part)
                ans.append(" ".join(cons))
                cons.pop()
            if part == "":
                ans.append(" ".join(cons))
                return

            def check(s):
                dp = [False] * (len(s)+1)
                dp[0] = True
                for i in range(1, len(s)+1):
                    for j in range(i):
                        if dp[j] and s[j:i] in words:
                            dp[i] = True
                return dp[-1]
            
            if check(part):
                M = len(part)
                amt = 0
                possible = False
                for i in range(M):
                    p = part[:i]
                    if p in words:
                        cons.append(p)
                        go(cons,part[i:])
                        cons.pop()

        
        for i in range(N+1):
            p = s[:i]
            if p in words:
                go([p], s[i:])
        
        #ans.sort()
        return ans
        
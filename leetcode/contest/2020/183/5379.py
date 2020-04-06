class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [[],[],[]] # take 3, 2, 1 stone
        for i in range(0, len(stoneValue)):
            three = stoneValue[i]
            two = stoneValue[i]
            one = stoneValue[i]
            if i+1 < len(stoneValue):
                three += stoneValue[i+1]
                two += stoneValue[i+1]
            if i+2 < len(stoneValue):
                three += stoneValue[i+2]
            dp[0].append(three)
            dp[1].append(two)
            dp[2].append(one)
        #for r in dp:
            #print(r)
        
        best = [-float('inf') for i in range(0, len(stoneValue))]
        best[-1] = max(dp[0][-1], dp[1][-1], dp[2][-1])
        for i in range(len(stoneValue)-2, -1, -1):
            if i == len(stoneValue)-2:
                best[i] = max(dp[0][i], dp[1][i], -best[i+1]+dp[2][i])
            elif i == len(stoneValue)-3:
                best[i] = max(dp[0][i], -best[i+2]+dp[1][i], -best[i+1]+dp[2][i])
            else:
                best[i] = max(-best[i+3]+dp[0][i], -best[i+2]+dp[1][i], -best[i+1]+dp[2][i])
        
        #print(best)
        if best[0] == 0:
            return "Tie"
        elif best[0] > 0:
            return "Alice"
        else:
            return "Bob"

# this is exactly the same as dp in c++ but still gets TLE

import sys

dp = [1 for _ in range(0, 1000001)]
m = [1 for _ in range(0, 11)]
dp[0] = 0
for line in sys.stdin:
    line = list(map(int, line.split()))
    n = line[0]
    for i in range(2, len(line)):
        m[i-2] = line[i]
    # Stan starts the game
    for i in range(1, n+1):
        dp[i] = 0
        for amt in m:
            if amt <= i and dp[i-amt] == 0:
                dp[i] = 1
                break
    print("Stan wins") if dp[n] == 1 else print("Ollie wins")

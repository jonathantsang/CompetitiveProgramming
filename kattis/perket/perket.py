n = int(input())

sr = []
br = []
for _ in range(0, n):
    s, b = list(map(int, input().split()))
    sr.append(s)
    br.append(b)

bestdiff = 1000000000
i = 1
while(i < (1 << n)):
    s, b = 1, 0
    for j in range(0, n):
        if ((1 << j) & i):
            s *= sr[j]
            b += br[j]
    bestdiff = min(bestdiff, abs(s-b))
    i+=1
print(bestdiff)

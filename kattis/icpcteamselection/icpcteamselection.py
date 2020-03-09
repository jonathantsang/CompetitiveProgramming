t = int(input())

for _ in range(0, t):
    n = int(input())
    vals = sorted(list(map(int, input().split())), reverse=True)
    best = 0
    for i in range(0, n):
        best += vals[i*2+1]
    print(best)

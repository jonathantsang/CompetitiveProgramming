# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

t = rri()
for i in range(t):
    if i&1:
        print(i)

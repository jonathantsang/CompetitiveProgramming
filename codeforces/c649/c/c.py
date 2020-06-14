from collections import deque

n = int(input())

INF=float('inf')

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N, A):
    free = deque()
    ans = [-1] * N
    low = 0
    for i, x in enumerate(A):
        free.append([i, x])
        while low < x:
            if not free: return
            j, y = free.pop()
            if low != y:  #success
                ans[j] = low
                low += 1
            else: return

    while free:
        ans[free.pop()[0]] = 10**6
    return ans


arr= rrm()
ans = solve(n,arr)
if ans is None:
    print -1
else:
    print(" ".join(map(str, ans)))


# from awice

from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(K,M,TAKEN,NEEDED,C):
    #print(K,M,TAKEN,NEEDED,C)
    for i in range(M):
        ss = TAKEN & C[i]
        if len(ss) < NEEDED[i]:
            return "no"
    return "yes"

v = "abc"
while True:
    v = rrm()
    #print(v)
    if len(v) == 1 and v[0] == 0:
        break

    K,M = v
    TAKEN = set(rrm())
    categories = defaultdict(set)
    NEEDED = defaultdict(int) # category -> # needed
    for i in range(M):
        N,NEED,*COURSES = rrm()
        NEEDED[i] = NEED
        #print(COURSES)
        categories[i] = set(COURSES)

    print(solve(K,M, TAKEN, NEEDED, categories))

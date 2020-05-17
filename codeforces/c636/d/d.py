import sys
input = sys.stdin.readline
from itertools import accumulate

t=int(input())
for tests in range(t):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    ANS=[0]*(k*2+3)

    for i in range(n//2):
        x,y=A[i],A[n-1-i]
        if x>y:
            x,y=y,x

        #print(x,y)

        ANS[x+1]-=1
        ANS[y+k+1]+=1
        ANS[x+y]-=1
        ANS[x+y+1]+=1

        #print(ANS)

    #print(ANS)

    total = 0
    best = float('inf')
    for v in ANS:
    	total += v
    	best = min(best, total)
    #print(S)

    print(n+best)

    
        
            


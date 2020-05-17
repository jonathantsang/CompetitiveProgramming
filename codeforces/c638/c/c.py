# cook your dish here
from collections import defaultdict
 
t=int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    s=input()
    s1=s
    s=sorted(s)
    m=list(set(s))
    x=max(s[:k])
    y=min(s[:k])
    if x==y:
        if len(list(set(s[k:])))==1:
            ans1=''
            for i in range(0,n,k):
                ans1=ans1+s[i]
            ans=''
            for i in range(k-1,n,k):
                ans=ans+s[i]
            print(max(ans,ans1))
        else:
            for i in range(k,n):
                y=y+s[i]
            print(y)
    else:
        print(x)
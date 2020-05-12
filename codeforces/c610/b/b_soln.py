f=int(input())
for j in range(f):
	n,p,k=list(map(int,input().split()))
	l=list(map(int,input().split()))
	l.sort()
	ans=0
	dp=[0,l[0]]
	del l[0]
	countt=-1
	for i in l:
		dp.append(dp[countt+1]+i)
		countt+=1
	for i in range(len(dp)):
		if(dp[i]<=p):
			ans=i
	print(ans)

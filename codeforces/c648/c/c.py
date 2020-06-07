n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = [0] * n # difference in distance between a value in a and b
out = [0] * n # number of occurences for distance in value from a to b
for i in range(n):
	diff[a[i]-1]+=i
for i in range(n):
	diff[b[i]-1]-=i
for v in diff:
	out[v] += 1
print(max(out))

# by conqueror_of_tourist

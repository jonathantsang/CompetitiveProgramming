import sys

m = 10000000 + 7 # 10e9 + 7

nk = sys.stdin.readline().split()
n = int(nk[0])
k = int(nk[1])

a = sys.stdin.readline()[:-1] ## \n

aon = 0
firstzero = -1
i = 0
for digit in a:
	if digit == '1':
		aon += 1
	if digit == '0' and firstzero == -1:
		firstzero = i
	i += 1

possible = 0

ans = {}

def recurse(a, idx, needed, have, soln, carry):
	global possible
	global ans
	print(a, idx, soln, needed, have, carry)
	if soln in ans:
		return
	ans[soln] = 1
	if idx == -1:
		if needed == have:
			print(soln)
			possible += 1
			possible %= m
		return
	if a[idx] == '0':
		if carry == '1':
			# Picking 1 will carry by 1
			recurse(a, idx-1, needed, have, '1' + soln, '1') # pick 1
			# Pick 0
			recurse(a, idx-1, needed, have+1, '0' + soln, '0')
		else:
			recurse(a, idx-1, needed, have+1,'1' + soln, '0') # pick 1
			# Pick 0
			recurse(a, idx-1, needed, have, '0' + soln, '0')		

	elif a[idx] == '1':
		if carry == '1':
			# Picking 1 will carry by 1, keep same since carried 1, but also add 1
			recurse(a, idx-1, needed, have+1, '1' + soln, '1')
			# Pick 0
			recurse(a, idx-1, needed, have, '0' + soln, '1')
		else:
			# No carry so it will be 1
			recurse(a, idx-1, needed, have, '1' + soln, '1') # Pick 1
			# Pick 0
			recurse(a, idx-1, needed, have+1, '0' + soln, '0')# Pick 0	

recurse(a, len(a)-1, k, 0, "", '0') # Shift means it still can overflow N

print(possible)
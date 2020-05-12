t = int(input())

def solve(n, k):
	if k > n:
		print("NO")
		return
	elif n % k == 0:
		# all n // k value
		print("YES")
		ans = [n // k for _ in range(k)]
		print(" ".join(list(map(str, ans))))
		return
	else:
		# check reg
		div = n // k
		leftover = n - div * (k - 1)
		if leftover > 0 and div > 0 and leftover % 2 == div % 2:
			print("YES")
			ans = [n // k for _ in range(k-1)]
			ans.append(leftover)
			print(" ".join(list(map(str, ans))))
			return

		# check other
		div = n // k + 1
		leftover = n - div * (k - 1)
		if leftover > 0 and div > 0 and leftover % 2 == div % 2:
			print("YES")
			ans = [n // k + 1 for _ in range(k-1)]
			ans.append(leftover)
			print(" ".join(list(map(str, ans))))
			return

		# check other
		div = n // k - 1
		leftover = n - div * (k - 1)
		if leftover > 0 and div > 0 and leftover % 2 == div % 2:
			print("YES")
			ans = [n // k - 1 for _ in range(k-1)]
			ans.append(leftover)
			print(" ".join(list(map(str, ans))))
			return

		else:
			print("NO")
			return

	# yes or no

for _ in range(t):
	n, k = list(map(int, input().split()))
	solve(n, k)
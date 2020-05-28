from string import ascii_lowercase
t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, m, words):
	def neighbors(word):
		ans = {word}
		for i in range(m):
			for c in ascii_lowercase:
				ans.add(word[:i] + c + word[i+1:])
		return ans

	intersection = neighbors(words[0])
	for i in range(1, n):
		intersection &= neighbors(words[i])

	if not intersection:
		return "-1"
	return intersection.pop()

for _ in range(t):
	n, m = list(map(int, input().split()))
	arr = []
	for _ in range(n):
		arr.append(input())
	print(solve(n, m, arr))

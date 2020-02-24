import sys

p, tests = list(map(int, sys.stdin.readline().split()))

score = 0
for _ in range(0, p):
    s = [input().strip() for _ in range(tests)]
    if all(t[0].lower() + t[1:] == t.lower() for t in s):
        score += 1
print(score)

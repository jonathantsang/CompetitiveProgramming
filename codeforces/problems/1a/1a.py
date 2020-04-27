import math

n, m, a = list(map(int, input().split()))
print(math.ceil(n / a) * math.ceil(m / a))

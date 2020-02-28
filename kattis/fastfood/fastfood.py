t = int(input())

for _ in range(0, t):
    n, m = list(map(int, input().split()))
    prizes = {} # prize (stickers) -> value
    for i in range(0, n):
        n, *stickers, value = map(int, input().split())
        prizes[tuple(stickers)] = value
    collected = {(i+1):v for i, v in enumerate(map(int, input().split()))}
    total = 0
    for needed in prizes:
        a = min(collected[i] for i in needed)
        total += a*prizes[needed]
    print(total)

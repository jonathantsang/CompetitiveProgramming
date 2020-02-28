events = list(input())

ans = 0
for i, c in enumerate(events):
    start = c
    seen = {}
    for j in range(i+1, len(events)):
        if events[j] == start:
            break
        if events[j] not in seen:
            seen[events[j]] = 1
            ans += 1
print(ans)

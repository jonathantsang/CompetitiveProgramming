o = int(input())
orders = []

timeline = {} # time -> actions
for _ in range(0, o):
    d, t = list(map(int, input().split()))
    orders.append((d, t))

    if t in timeline:
        timeline[t] += 1
    else:
        timeline[t] = 1
    if t - d in timeline:
        timeline[t-d] += 1
    else:
        timeline[t-d] = 1
    if t - 2 * d in timeline:
        timeline[t-2*d] += 1
    else:
        timeline[t-2*d] = 1

most = 0
for time in timeline:
    most = max(most, timeline[time])

print(most // 2 + most % 2)

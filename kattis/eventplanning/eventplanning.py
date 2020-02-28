n, b, h, w = list(map(int, input().split()))

costs = [] # (cost, [beds free on weekends])
for i in range(0, h):
    cost = int(input())
    beds = list(map(int, input().split()))
    costs.append((cost, beds))

mincost = float('inf')
for cost in costs:
    if cost[0] * n < b and cost[0] * n < mincost:
        possible = False
        for weekend in cost[1]:
            if weekend >= n:
                possible = True
                break
        if possible:
            mincost = cost[0] * n

print(mincost) if mincost != float('inf') else print("stay home")

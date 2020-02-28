import heapq

n, k = list(map(int, input().split()))

# stored as tuples with (attack/defense/hp, index)
attack = []
defense = []
hp = []

for i in range(0, n):
    a, d, h = list(map(int, input().split()))
    attack.append((-a, i))
    defense.append((-d, i))
    hp.append((-h, i))

heapq.heapify(attack)
heapq.heapify(defense)
heapq.heapify(hp)

total = {} # id -> 1
for _ in range(0, k):
    val = heapq.heappop(attack)
    total[val[1]] = 1
for _ in range(0, k):
    val = heapq.heappop(defense)
    total[val[1]] = 1
for _ in range(0, k):
    val = heapq.heappop(hp)
    total[val[1]] = 1

print(len(total))

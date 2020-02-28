cards = [int(n) for n in input().split()]
num_dealt = int(input())

present = [1 if cards[n] > 0 else 0 for n in range(10)]
num_after = [sum(present[n:]) for n in range(10)]

passes = [[0 for m in range(10)] for n in range(num_dealt - 1)]
passes.append(cards)

for p in range(num_dealt - 2, -1, -1):
    for i in range(10):
        if num_after[i] >= num_dealt - p:
            for j in range(i + 1, 10):
                passes[p][i] += cards[i] * passes[p+1][j]

print(sum(passes[0]))

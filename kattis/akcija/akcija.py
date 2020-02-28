n = int(input())
vals = []
for _ in range(0, n):
    vals.append(int(input()))
vals = sorted(vals, reverse=True)
price = sum(vals)
for i in range(2, len(vals), 3):
    price -= vals[i]
print(price)
